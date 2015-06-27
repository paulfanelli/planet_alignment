"""
.. module:: cmd_parser
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
import pytest
from planet_alignment.cmd.cmd_parser import CommandParser
from planet_alignment.test import constants


@pytest.fixture(scope='module')
def fix_parser():
    return CommandParser()


def test_nonexistent_config_file(fix_parser):
    with pytest.raises(SystemExit):
        fix_parser.parse('--config foobar'.split())


def test_nonexistent_plugins_file(fix_parser):
    with pytest.raises(SystemExit):
        fix_parser.parse('--plugins abc.py'.split())


def test_wrong_type_plugins_file(fix_parser):
    with pytest.raises(SystemExit):
        foo_txt_file = constants.TEST_WRONG_PLUGIN_FILE_TYPE
        fix_parser.parse('--plugins {}'.format(foo_txt_file).split())


def test_valid_options(fix_parser):
    test_etc_dir = constants.TEST_ETC_DIR
    config_file = constants.TEST_SYSTEM_YAML
    plugins = '{0}/foo.py {0}/bar.py'.format(test_etc_dir)
    plugins_list = [
        '{}/foo.py'.format(test_etc_dir),
        '{}/bar.py'.format(test_etc_dir)
    ]
    parsed = fix_parser.parse('--config {} --plugins {} --time 10'.format(config_file, plugins).split())
    assert parsed.config == config_file
    assert parsed.plugins == plugins_list
    assert parsed.time == 10

def test_valid_options_short_opts(fix_parser):
    test_etc_dir = constants.TEST_ETC_DIR
    config_file = constants.TEST_SYSTEM_YAML
    plugins = '{0}/foo.py {0}/bar.py'.format(test_etc_dir)
    plugins_list = [
        '{}/foo.py'.format(test_etc_dir),
        '{}/bar.py'.format(test_etc_dir)
    ]
    parsed = fix_parser.parse('-c {} -p {} -t 10'.format(config_file, plugins).split())
    assert parsed.config == config_file
    assert parsed.plugins == plugins_list
    assert parsed.time == 10
