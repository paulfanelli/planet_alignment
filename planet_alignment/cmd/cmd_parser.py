"""
.. module:: cmd_parser
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
import argparse
import os
from zope.interface import implements
from planet_alignment.cmd.interface import ICommandParser


class CommandParser(object):
    implements(ICommandParser)

    def __init__(self):
        self._parser = None
        self._create_parser()

    def _create_parser(self):
        parser = argparse.ArgumentParser(description='Planet Alignment application',
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('-c',
                            '--config',
                            action='store',
                            dest='config',
                            help='Planet alignment configuration file',
                            metavar='FILE',
                            required=True,
                            type=lambda arg: self._is_valid_file(arg))

        parser.add_argument('-p',
                            '--plugins',
                            action='store',
                            dest='plugins',
                            help='List of plugin python files',
                            nargs='+',
                            required=True,
                            type=lambda arg: self._is_valid_filelist(arg, extension='py'))

        parser.add_argument('-t',
                            '--time',
                            action='store',
                            dest='time',
                            help='The time to calculate the planet alignment for',
                            required=True,
                            type=int)
        self._parser = parser
        return self

    def _is_valid_file(self, arg, extension=None):
        """Validate that the argument passed is a valid file on the system"""
        arg = os.path.abspath(arg)
        if os.path.exists(arg):
            if extension:
                ext = arg.rpartition('.')[-1]
                if ext == 'py':
                    return arg
                else:
                    err = "The file '{}' has the wrong extension '{}'".format(arg, ext)
                    self._parser.error(err)
            return arg
        else:
            err = "The file '{}' does not exist".format(arg)
            self._parser.error(err)

    def _is_valid_filelist(self, arg, extension=None):
        """Validate that the argument passed is a valid file list"""
        arglist = []
        if isinstance(arg, str):
            arglist.append(arg)
        elif isinstance(arg, list):
            arglist = arg
        else:
            err = "Invalid arg list '{}'".format(arg)
            self._parser.error(err)

        retval_list = []
        for arg in arglist:
            arg = self._is_valid_file(arg, extension=extension)
            retval_list.append(arg)
        return ','.join(retval_list)

    def parse(self, args):
        return self._parser.parse_args(args)
