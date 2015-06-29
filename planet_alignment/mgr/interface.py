"""
.. module:: interface
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
from zope.interface import Interface


class IPluginsManager(Interface):
    """An interface to manage the plugins"""

    def get_plugin_class_by_path(path):
        """Get the plugin class by the plugin file path"""

    def get_plugin_instance_by_path(path):
        """Get the plugin class instance by the plugin file path"""

    def get_plugin_name_by_path(path):
        """Get the plugin name by the plugin file path"""
