"""
.. module:: alignment
   :platform: linux
   :synopsis: Test the main alignment program.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/28/15

"""
import pytest
from planet_alignment.alignment import main
from planet_alignment.test import constants


@pytest.fixture(scope='module',
                params=[0])
def fix_main(request):
    config_file = constants.TEST_SYSTEM_YAML
    plugins = constants.TEST_PLUGIN_ALIGN1
    arg_list = '--config {} --plugins {} --time {}'.format(config_file, plugins, request.param).split()
    return arg_list


def test_main(fix_main):
    main(fix_main)
