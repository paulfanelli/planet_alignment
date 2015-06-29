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


@pytest.fixture(scope='module',
                params=[0.0, 0.5, 10.0])
def fix_app(request):
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    plugins = PluginsManager(constants.TEST_PLUGIN_LIST_FOO_BAR)
    return App(sd, plugins, request.param)


@pytest.fixture(scope='module',
                params=[0, 0.0, 0.1, 0.5])
def fix_align1(request):
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    plugins = PluginsManager(constants.TEST_PLUGIN_LIST_ALIGN1)
    return App(sd, plugins, request.param)


@pytest.fixture(scope='module',
                params=[0])
def fix_align2(request):
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    plugins = PluginsManager(constants.TEST_PLUGIN_LIST_ALIGN2)
    return App(sd, plugins, request.param)


@pytest.fixture(scope='module',
                params=[0.1])
def fix_align2_2(request):
    config_file = constants.TEST_SYSTEM2_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    plugins = PluginsManager(constants.TEST_PLUGIN_LIST_ALIGN2)
    return App(sd, plugins, request.param)


@pytest.fixture(scope='module',
                params=[0.1])
def fix_align1_align2(request):
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    plugins = PluginsManager(constants.TEST_PLUGIN_LIST_ALIGN1_ALIGN2)
    return App(sd, plugins, request.param)


@pytest.fixture(scope='module',
                params=[2, 2.0, 10, 10.0])
def fix_align1_no_result(request):
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    plugins = PluginsManager(constants.TEST_PLUGIN_LIST_ALIGN1)
    return App(sd, plugins, request.param)


def test_app(fix_app):
    assert isinstance(fix_app._system_data, SystemData)
    assert len(fix_app._system_data) == 3
    assert isinstance(fix_app._plugins_mgr, PluginsManager)
    assert len(fix_app._plugins_mgr) == 2
    assert isinstance(fix_app._time, float)


def test_app_run(fix_app, capsys):
    fix_app.run()
    out, err = capsys.readouterr()
    assert "Plugin class not found" in str(out)


def test_align1_run(fix_align1):
    r = fix_align1.run()
    assert r[0] == 'align1: planet-A, planet-B'


def test_align1_run_no_result(fix_align1_no_result):
    r = fix_align1_no_result.run()
    assert r == []


def test_align2_run(fix_align2):
    r = fix_align2.run()
    # print(">>>>>>>>> r is {}".format(r))
    assert r[0] == 'align2: planet-A, planet-B'


def test_align2_2_run(fix_align2_2):
    r = fix_align2_2.run()
    # print(">>>>>>>>> r is {}".format(r))
    assert r[0] == 'align2: planet-A, planet-B\nalign2: planet-A, planet-B, planet-C\nalign2: planet-B, planet-C'


def test_align1_align2_run(fix_align1_align2):
    r = fix_align1_align2.run()
    # print(">>>>>>>>> r is {}".format(r))
    assert r[0] == 'align1: planet-A, planet-B'
    assert r[1] == 'align2: planet-A, planet-B'
