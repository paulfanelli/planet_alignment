"""
.. module:: config_parser
   :platform: linux
   :synopsis: Module to test the bunch YAML configuration parser.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
from bunch import Bunch
import pytest
from planet_alignment.config.bunch_parser import BunchParser
from planet_alignment.test import constants


@pytest.fixture(scope='module')
def fix_parser():
    return BunchParser()


def test_parse_nonexistent_file(fix_parser, capsys):
    with pytest.raises(SystemExit):
        fix_parser.parse('nonexistent')
    out, err = capsys.readouterr()
    assert "ERROR: No configuration file" in str(out)


def test_parse_bad_file(fix_parser, capsys):
    config_file = constants.TEST_BAD_CONFIG_FILE
    with pytest.raises(SystemExit):
        fix_parser.parse(config_file)
    out, err = capsys.readouterr()
    assert "ERROR: Error parsing the configuration file" in str(out)


def test_parse_config_file(fix_parser):
    config_file = constants.TEST_SYSTEM_YAML
    b = fix_parser.parse(config_file)
    assert isinstance(b, Bunch) is True
