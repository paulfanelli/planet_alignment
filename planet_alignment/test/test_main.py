"""
.. module:: alignment
   :platform: linux
   :synopsis: Test the main alignment program.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/28/15

"""
import pytest
from planet_alignment.__main__ import main
from planet_alignment.test import constants


@pytest.fixture(scope='module',
                params=[0, 0.0, 0.1, 0.5])
def fix_main(request):
    config_file = constants.TEST_SYSTEM_YAML
    plugins = constants.TEST_PLUGIN_ALIGN1
    arg_list = '--config {} --plugins {} --time {}'.format(config_file, plugins, request.param).split()
    return arg_list


@pytest.fixture(scope='module',
                params=[0.1])
def fix_main_align1_align2_2(request):
    config_file = constants.TEST_SYSTEM2_YAML
    plugins = "{} {}".format(constants.TEST_PLUGIN_ALIGN1, constants.TEST_PLUGIN_ALIGN2)
    arg_list = '--config {} --plugins {} --time {}'.format(config_file, plugins, request.param).split()
    return arg_list


@pytest.fixture(scope='module',
                params=[1.0, 2.0, 10.0, 20.0])
def fix_main_no_result(request):
    config_file = constants.TEST_SYSTEM_YAML
    plugins = constants.TEST_PLUGIN_ALIGN1
    arg_list = '--config {} --plugins {} --time {}'.format(config_file, plugins, request.param).split()
    return arg_list


def test_main(fix_main, capsys):
    main(fix_main)
    out, err = capsys.readouterr()
    assert "align1: planet-A, planet-B" in str(out)


def test_main_align1_align2(fix_main_align1_align2_2):
    main(fix_main_align1_align2_2)


def test_main_no_result(fix_main_no_result, capsys):
    main(fix_main_no_result)
    out, err = capsys.readouterr()
    assert not str(out)
