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

TEST_SYSTEM_YAML = join(TEST_ETC_DIR, 'system.yaml')
TEST_BAD_CONFIG_FILE = join(TEST_ETC_DIR, 'foo.py')
TEST_WRONG_PLUGIN_FILE_TYPE = join(TEST_ETC_DIR, 'foo.txt')
TEST_PLUGIN_FOO = join(TEST_ETC_DIR, 'foo.py')
TEST_PLUGIN_BAR = join(TEST_ETC_DIR, 'bar.py')
TEST_DEFAULT_ALIGNMENT_DELTA_DEGREES = constants.DEFAULT_ALIGNMENT_DELTA_DEGREES
