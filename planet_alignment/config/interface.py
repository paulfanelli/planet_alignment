"""
.. module:: interface
   :platform: linux
   :synopsis: An interface module to a YAML configuration file parser using the Bunch module.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
from zope.interface import Interface


class IBunchParser(Interface):
    """An interface to a YAML configuration file parser using the Bunch module."""

    def parse(path):
        """Parse the YAML configuration file"""
