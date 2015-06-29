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
    """This class houses the system data as a bunch object.

    The system data consists of a name, theta, radius and period for each planet.

    - **parameters** and **types**::

        :param data: The system data as a bunch object.
        :type data: Bunch object.
    """

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

    def __len__(self):
        return len(self.system)
