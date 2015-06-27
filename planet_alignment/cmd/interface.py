"""
.. module:: interface
   :platform: linux
   :synopsis: An interface to a command-line argument parser.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
from zope.interface import Interface


class ICommandParser(Interface):
    """An interface to a command-line parser"""

    def parse(args):
        """Parse the command-line arguments"""
