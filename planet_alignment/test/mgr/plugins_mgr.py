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


def test_get_plugin_module_by_path(fix_plug):
    # module foo contains a dummy foo value of 1
    mod = fix_plug.get_plugin_module_by_path(constants.TEST_PLUGIN_FOO)
    assert mod.foo == 1


def test_get_plugin_module_by_bad_path(fix_plug):
    with pytest.raises(KeyError):
        fix_plug.get_plugin_module_by_path("bad_path")
