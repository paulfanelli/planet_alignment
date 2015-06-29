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

    def run():
        """Run the planet alignment and return the results"""

    def print_results(results):
        """Print the results to the screen"""


class IAppFactory(Interface):
    """An interface to an application factory"""

    def create():
        """return a created Application object"""
