"""
.. module:: __main__
   :platform: linux
   :synopsis: Special main entry point.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/28/15

"""
import sys
from planet_alignment.app.app_factory import AppFactory
from planet_alignment.cmd.cmd_parser import CommandParser


def main(argv=None):
    """The main function"""
    if argv is None:
        argv = sys.argv[1:]

    cmd_args = CommandParser().parse(argv)
    app = AppFactory(cmd_args).create()
    results = app.run()
    if results:
        app.print_results(results)


if __name__ == "__main__":
    sys.exit(main())
