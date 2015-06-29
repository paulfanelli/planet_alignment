"""
.. module:: system_data
   :platform: linux
   :synopsis: A module to test the system data object.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
from bunch import Bunch

import pytest
from planet_alignment.config.bunch_parser import BunchParser
from planet_alignment.data.system_data import SystemData
from planet_alignment.test import constants


@pytest.fixture(scope='module')
def fix_sd():
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    return SystemData(data)


def test_system_data(fix_sd):
    it = iter(fix_sd)
    item = it.next()
    assert isinstance(item, Bunch)
    assert item.name == 'planet-A'
    assert item.theta == 0
    assert item.radius == 1
    assert item.period == 20

    item = it.next()
    assert isinstance(item, Bunch)
    assert item.name == 'planet-B'
    assert item.theta == 0
    assert item.radius == 5
    assert item.period == 30

    item = it.next()
    assert isinstance(item, Bunch)
    assert item.name == 'planet-C'
    assert item.theta == 2
    assert item.radius == 10
    assert item.period == 60


def test_system_data_len(fix_sd):
    assert len(fix_sd) == 3


def test_none_system_data(capsys):
    with pytest.raises(SystemExit):
        SystemData(None)
    out, err = capsys.readouterr()
    assert "object is not iterable" in str(out)


def test_bad_system_data(capsys):
    with pytest.raises(SystemExit):
        SystemData("abc")
    out, err = capsys.readouterr()
    assert "Unknown exception" in str(out)
