"""
.. module:: plugins_mgr
   :platform: linux
   :synopsis: A module to manage the plugins.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
from zope.interface import implements
from planet_alignment.mgr.interface import IPluginsManager


class PluginsManager(object):
    implements(IPluginsManager)

    def __init__(self, plugins):
        assert isinstance(plugins, list)
        self._plugins = plugins

    def __iter__(self):
        return iter(self._plugins)

    def __len__(self):
        return len(self._plugins)
