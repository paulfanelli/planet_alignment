"""
.. module:: plugins_mgr
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
import pytest
from planet_alignment.mgr.plugins_mgr import PluginsManager
from planet_alignment.test import constants


@pytest.fixture(scope='module')
def fix_plug():
    plugins_list = constants.TEST_PLUGIN_LIST_FOO_BAR
    return PluginsManager(plugins_list)


def test_valid_plugins_list(fix_plug):
    it = iter(fix_plug)
    item = it.next()
    assert item == constants.TEST_PLUGIN_FOO

    item = it.next()
    assert item == constants.TEST_PLUGIN_BAR


def test_valid_plugins_len(fix_plug):
    assert len(fix_plug) == 2


def test_invalid_plugins_list():
    with pytest.raises(AssertionError):
        PluginsManager(10)
