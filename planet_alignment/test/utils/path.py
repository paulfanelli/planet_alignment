"""
.. module:: path
   :platform: linux
   :synopsis: Module to test getting all of the various project directories.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/26/15

"""
from os.path import join
from planet_alignment.utils import path


def test_get_projects_dir():
    """
    Only uncomment to test on my system, leave commented out so others can run all the tests.
    Once I've verified that it works, I can now use it below to get the projects dir, which will
    also include the user's home dir.
    """
    # assert path.get_projects_dir() == '/home/pfanelli/python-devel'
    pass


PROJECTS_DIR = path.get_projects_dir()


def test_get_root_dir():
    assert path.get_root_dir() == join(PROJECTS_DIR, 'planet_alignment')


def test_get_bin_dir():
    assert path.get_bin_dir() == join(PROJECTS_DIR, 'planet_alignment', 'bin')


def test_get_etc_dir():
    assert path.get_etc_dir() == join(PROJECTS_DIR, 'planet_alignment', 'etc')


def test_get_plugins_dir():
    assert path.get_plugins_dir() == join(PROJECTS_DIR, 'planet_alignment', 'plugins')


def test_get_src_dir():
    assert path.get_src_dir() == join(PROJECTS_DIR, 'planet_alignment', 'planet_alignment')


def test_get_test_dir():
    assert path.get_test_dir() == join(PROJECTS_DIR, 'planet_alignment', 'planet_alignment', 'test')


def test_get_test_etc_dir():
    assert path.get_test_etc_dir() == join(PROJECTS_DIR, 'planet_alignment', 'planet_alignment', 'test', 'etc')
