"""
.. module:: app_factory
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
from zope.interface import implements
from planet_alignment.app.app import App
from planet_alignment.app.interface import IAppFactory
from planet_alignment.config.bunch_parser import BunchParser
from planet_alignment.data.system_data import SystemData
from planet_alignment.mgr.plugins_mgr import PluginsManager


class AppFactory(object):
    implements(IAppFactory)

    def __init__(self, cmd_args):
        data = BunchParser().parse(cmd_args.config)
        self._system_data = SystemData(data)
        self._plugins = PluginsManager(cmd_args.plugins)
        self._time = cmd_args.time

    def create(self):
        return App(self._system_data, self._plugins, self._time)
