"""
.. module:: plugins_mgr
   :platform: linux
   :synopsis: A module to manage the plugins.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
import importlib
import inspect
import sys
from zope.interface import implements
from planet_alignment.mgr.interface import IPluginsManager
from planet_alignment.utils.path import get_path_parts_tuple


def append_sys_path(path):
    if path not in sys.path:
        sys.path.append(path)


class PluginsManager(object):
    implements(IPluginsManager)

    def __init__(self, plugins):
        assert isinstance(plugins, list)
        self._plugins = plugins
        self._plugin_modules = {}
        self._load_plugin_modules()

    def _load_plugin_modules(self):
        for plugin_path in self._plugins:
            try:
                mod_dir, mod_file, mod_name, mod_ext = get_path_parts_tuple(plugin_path)
                append_sys_path(mod_dir)
                imp_mod = importlib.import_module(mod_name)
                self._plugin_modules[plugin_path] = imp_mod
            except ImportError as ie:
                print("ERROR: Error importing module '{}'!".format(plugin_path))
                sys.exit("ERROR: {}".format(ie))
            except Exception as e:
                print("ERROR: Unknown error loading plugin module '{}'".format(plugin_path))
                sys.exit("ERROR: {}".format(e))

    def _get_plugin_module_by_path(self, path):
        try:
            return self._plugin_modules[path]
        except KeyError as ke:
            print("WARNING: Plugin module {} not found.".format(ke))
            raise

    def _get_plugin_class_name(self, module):
        clsmembers = inspect.getmembers(module, inspect.isclass)
        if len(clsmembers) == 0:
            raise AttributeError("Plugin class not found")
        if len(clsmembers) == 1:
            # there is only one class, return it's name
            return clsmembers[0][0]
        else:
            # there is more that one, iterate through,
            # returning the 1st non-base class
            for c in clsmembers:
                clsname = c[0]
                if clsname != "BasePlugin":
                    return clsname

    def get_plugin_class_by_path(self, path):
        mod = self._get_plugin_module_by_path(path)
        clsname = self._get_plugin_class_name(mod)
        return getattr(mod, clsname)

    def get_plugin_instance_by_path(self, path):
        cls = self.get_plugin_class_by_path(path)
        return cls()

    def get_plugin_name_by_path(self, path):
        self._get_plugin_module_by_path(path)
        _, _, mod_name, _ = get_path_parts_tuple(path)
        return mod_name

    def __iter__(self):
        return iter(self._plugins)

    def __len__(self):
        return len(self._plugins)
