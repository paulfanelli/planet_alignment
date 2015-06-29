"""
.. module:: plugins_mgr
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
import inspect
import pytest
from planet_alignment.mgr.plugins_mgr import PluginsManager
from planet_alignment.test import constants


@pytest.fixture(scope='module')
def fix_plug():
    plugins_list = constants.TEST_PLUGIN_LIST_FOO_BAR
    return PluginsManager(plugins_list)


@pytest.fixture(scope='module')
def fix_align1():
    plugins_list = constants.TEST_PLUGIN_LIST_ALIGN1
    return PluginsManager(plugins_list)


@pytest.fixture(scope='module')
def fix_base():
    plugins_list = constants.TEST_PLUGIN_LIST_BASE
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
    mod = fix_plug._get_plugin_module_by_path(constants.TEST_PLUGIN_FOO)
    assert mod.foo == 1


def test_get_plugin_module_by_bad_path(fix_plug, capsys):
    with pytest.raises(KeyError):
        fix_plug._get_plugin_module_by_path('bad_path')
    out, err = capsys.readouterr()
    assert "WARNING: Plugin module 'bad_path' not found." in str(out)


def test_get_plugin_class_by_path(fix_plug, capsys):
    with pytest.raises(KeyError):
        fix_plug.get_plugin_class_by_path('bad_path')
    out, err = capsys.readouterr()
    assert "WARNING: Plugin module 'bad_path' not found." in str(out)


def test_get_plugin_instance_by_path(fix_plug, capsys):
    with pytest.raises(KeyError):
        fix_plug.get_plugin_instance_by_path('bad_path')
    out, err = capsys.readouterr()
    assert "WARNING: Plugin module 'bad_path' not found." in str(out)


def test_align1_get_plugin_class_name(fix_align1):
    mod = fix_align1._get_plugin_module_by_path(constants.TEST_PLUGIN_ALIGN1)
    clsname = fix_align1._get_plugin_class_name(mod)
    assert clsname == 'Align1Plugin'


def test_align1_get_plugin_class_by_path(fix_align1):
    cls = fix_align1.get_plugin_class_by_path(constants.TEST_PLUGIN_ALIGN1)
    c, t = inspect.getmembers(cls, inspect.isclass)[0]
    assert c == '__class__'
    assert isinstance(t, type)
    assert "are_planets_aligned" in dir(cls)


def test_align1_get_plugin_instance_by_path(fix_align1):
    inst = fix_align1.get_plugin_class_by_path(constants.TEST_PLUGIN_ALIGN1)
    c, t = inspect.getmembers(inst, inspect.isclass)[0]
    assert c == '__class__'
    assert isinstance(t, type)
    assert "are_planets_aligned" in dir(inst)


def test_align1_get_plugin_name_by_path(fix_align1):
    name = fix_align1.get_plugin_name_by_path(constants.TEST_PLUGIN_ALIGN1)
    assert name == 'align1'


def test_base_get_plugin_class_name(fix_base):
    mod = fix_base._get_plugin_module_by_path(constants.TEST_PLUGIN_BASE)
    clsname = fix_base._get_plugin_class_name(mod)
    assert clsname == 'BasePlugin'


def test_base_get_plugin_class_by_path(fix_base):
    cls = fix_base.get_plugin_class_by_path(constants.TEST_PLUGIN_BASE)
    c, t = inspect.getmembers(cls, inspect.isclass)[0]
    assert c == '__class__'
    assert isinstance(t, type)
    assert "are_planets_aligned" in dir(cls)


def test_base_get_plugin_instance_by_path(fix_base):
    inst = fix_base.get_plugin_class_by_path(constants.TEST_PLUGIN_BASE)
    c, t = inspect.getmembers(inst, inspect.isclass)[0]
    assert c == '__class__'
    assert isinstance(t, type)
    assert "are_planets_aligned" in dir(inst)


def test_base_get_plugin_name_by_path(fix_base):
    name = fix_base.get_plugin_name_by_path(constants.TEST_PLUGIN_BASE)
    assert name == 'base'


def test_base_get_plugin_name_by_path_bad_name(fix_base):
    with pytest.raises(KeyError):
        fix_base.get_plugin_name_by_path("bad_name")
