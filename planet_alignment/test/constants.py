"""
.. module:: constants
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
from os.path import join
from planet_alignment import constants
from planet_alignment.utils import path

TEST_ETC_DIR = path.get_test_etc_dir()
TEST_PLUGINS_DIR = path.get_plugins_dir()

TEST_SYSTEM_YAML = join(TEST_ETC_DIR, 'system.yaml')
TEST_SYSTEM2_YAML = join(TEST_ETC_DIR, 'system2.yaml')
TEST_BAD_CONFIG_FILE = join(TEST_ETC_DIR, 'foo.py')
TEST_WRONG_PLUGIN_FILE_TYPE = join(TEST_ETC_DIR, 'foo.txt')
TEST_PLUGIN_FOO = join(TEST_ETC_DIR, 'foo.py')
TEST_PLUGIN_BAR = join(TEST_ETC_DIR, 'bar.py')
TEST_PLUGIN_LIST_FOO_BAR = [
    TEST_PLUGIN_FOO,
    TEST_PLUGIN_BAR
]
TEST_PLUGIN_ALIGN1 = join(TEST_ETC_DIR, 'align1.py')
TEST_PLUGIN_LIST_ALIGN1 = [
    TEST_PLUGIN_ALIGN1
]
TEST_PLUGIN_ALIGN2 = join(TEST_ETC_DIR, 'align2.py')
TEST_PLUGIN_LIST_ALIGN2 = [
    TEST_PLUGIN_ALIGN2
]
TEST_PLUGIN_BASE = join(TEST_PLUGINS_DIR, 'base.py')
TEST_PLUGIN_LIST_BASE = [
    TEST_PLUGIN_BASE
]
TEST_DEFAULT_ALIGNMENT_DELTA_DEGREES = constants.DEFAULT_ALIGNMENT_DELTA_DEGREES
