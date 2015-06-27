"""
.. module:: system_data
   :platform: linux
   :synopsis: The module containing the system data.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
import bunch
import sys
from yaml.parser import ParserError
from zope.interface import implements
from planet_alignment.data.interface import ISystemData


class SystemData(bunch.Bunch):
    implements(ISystemData)

    def __init__(self, data):
        try:
            super(SystemData, self).__init__(data)
        except ParserError as pe:
            print("ERROR: Error parsing data!")
            sys.exit("ERROR: {}".format(pe))
        except Exception as e:
            print("ERROR: Unknown exception '{}'".format(e))
            sys.exit("ERROR: {}".format(e))

    def __iter__(self):
        return iter(self.system)