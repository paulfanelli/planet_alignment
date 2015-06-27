"""
.. module:: constants
   :platform: linux
   :synopsis: 

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
from os.path import join
from planet_alignment.utils import path

TEST_ETC_DIR = path.get_test_etc_dir()

TEST_SYSTEM_YAML = join(TEST_ETC_DIR, 'system.yaml')
TEST_BAD_CONFIG_FILE = join(TEST_ETC_DIR, 'foo.py')
