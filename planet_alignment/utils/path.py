"""
.. module:: path
   :platform: linux
   :synopsis: Module to get all of the various project directories.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
import os
from os.path import dirname, join

PROJECTS_DIR = dirname(dirname(dirname(dirname(__file__))))
ROOT_DIR = dirname(dirname(dirname(__file__)))
BIN_DIR = join(ROOT_DIR, 'bin')
ETC_DIR = join(ROOT_DIR, 'etc')
SRC_DIR = dirname(dirname(__file__))
PLUGINS_DIR = join(SRC_DIR, 'plugins')
TEST_DIR = join(SRC_DIR, 'test')
TEST_ETC_DIR = join(TEST_DIR, 'etc')


def get_projects_dir():
    return PROJECTS_DIR


def get_root_dir():
    return ROOT_DIR


def get_bin_dir():
    return BIN_DIR


def get_etc_dir():
    return ETC_DIR


def get_src_dir():
    return SRC_DIR


def get_plugins_dir():
    return PLUGINS_DIR


def get_test_dir():
    return TEST_DIR


def get_test_etc_dir():
    return TEST_ETC_DIR


def get_path_parts_tuple(path):
    dir_part, file_part = os.path.split(path)
    name_part, ext_part = os.path.splitext(file_part)
    return dir_part, file_part, name_part, ext_part
