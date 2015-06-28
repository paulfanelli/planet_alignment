"""
.. module:: app
   :platform: linux
   :synopsis: The module to test the App.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
import pytest
from planet_alignment.app.app import App
from planet_alignment.config.bunch_parser import BunchParser
from planet_alignment.data.system_data import SystemData
from planet_alignment.mgr.plugins_mgr import PluginsManager
from planet_alignment.test import constants


@pytest.fixture(scope='module')
def fix_app():
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    plugins = PluginsManager(constants.TEST_PLUGIN_LIST_FOO_BAR)
    return App(sd, plugins, 0)


@pytest.fixture(scope='module')
def fix_align1():
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    plugins = PluginsManager(constants.TEST_PLUGIN_LIST_ALIGN1)
    return App(sd, plugins, 0)


def test_app(fix_app):
    assert isinstance(fix_app._system_data, SystemData)
    assert len(fix_app._system_data) == 3
    assert isinstance(fix_app._plugins, PluginsManager)
    assert len(fix_app._plugins) == 2
    assert isinstance(fix_app._time, int)
    assert fix_app._time == 0


def test_app_run(fix_app, capsys):
    fix_app.run()
    out, err = capsys.readouterr()
    assert "object has no attribute" in str(out)


def test_align1_run(fix_align1):
    r = fix_align1.run()
    assert r[0] == 'align1: planet-A, planet-B\n'
