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
    implements(IBunchParser)

    def __init__(self):
        self._data = None

    def parse(self, path):
        try:
            with open(path) as f:
                self._data = fromYAML(f)
        except IOError as ioe:
            print("ERROR: No configuration file '{}' found!".format(path))
            sys.exit("ERROR: {}".format(ioe))
        except ParserError as pe:
            print("ERROR: Error parsing the configuration file '{}'!".format(path))
            sys.exit("ERROR: {}".format(pe))
        except Exception, e:
            print("ERROR: Unknown exception '{}'".format(e))
            sys.exit("ERROR: {}".format(e))
        return self._data
