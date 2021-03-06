"""
.. module:: config_parser
   :platform: linux
   :synopsis: Module to parse a YAML configuration file using the bunch module.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
from bunch import fromYAML
import sys
from yaml.parser import ParserError
from zope.interface import implements
from planet_alignment.config.interface import IBunchParser


class BunchParser(object):
    """This class handles the parsing the system data using the bunch library module.

    - **parameters** and **types**::

        None.
    """

    implements(IBunchParser)

    def __init__(self):
        self._data = None

    def parse(self, path):
        """Parse the system data contained in a YAML configuration file.

            :param path: The path to the YAML configuration file.
            :type path: str
            :return: Returns the parsed system data as a Bunch object.
            :rtype: Bunch object.
        """
        try:
            with open(path) as f:
                self._data = fromYAML(f)
        except IOError as ioe:
            print("ERROR: No configuration file '{}' found!".format(path))
            sys.exit("ERROR: {}".format(ioe))
        except ParserError as pe:
            print("ERROR: Error parsing the configuration file '{}'!".format(path))
            sys.exit("ERROR: {}".format(pe))
        except Exception as e:
            print("ERROR: Unknown exception '{}'".format(e))
            sys.exit("ERROR: {}".format(e))
        return self._data
