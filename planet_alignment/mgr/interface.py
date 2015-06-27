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
