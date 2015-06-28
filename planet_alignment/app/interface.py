"""
.. module:: interface
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
from zope.interface import Interface


class IApp(Interface):
    """An interface to an application"""


class IAppFactory(Interface):
    """An interface to an application factory"""

    def create():
        """return a created Application object"""
