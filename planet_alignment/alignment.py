"""
.. module:: alignment
   :platform: linux
   :synopsis: The main planet alignment program.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
import sys
from planet_alignment.app.app_factory import AppFactory
from planet_alignment.cmd.cmd_parser import CommandParser


def main(argv):
    cmd_args = CommandParser().parse(argv)
    app = AppFactory(cmd_args).create()
    results = app.run()
    print('\n')
    for line in results:
        print(line)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
