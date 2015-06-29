"""
.. module:: app_factory
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
import pytest
from planet_alignment.app.app import App
from planet_alignment.app.app_factory import AppFactory
from planet_alignment.cmd.cmd_parser import CommandParser
from planet_alignment.test import constants


@pytest.fixture(scope='module')
def fix_af():
    test_etc_dir = constants.TEST_ETC_DIR
    config_file = constants.TEST_SYSTEM_YAML
    plugins = '{0}/foo.py {0}/bar.py'.format(test_etc_dir)
    arg_str = '--config {} --plugins {} --time 0.5'.format(config_file, plugins).split()
    cmd_args = CommandParser().parse(arg_str)
    return AppFactory(cmd_args)


def test_create(fix_af):
    app = fix_af.create()
    assert isinstance(app, App)
