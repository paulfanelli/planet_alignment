"""
.. module:: base
   :platform: linux
   :synopsis: Module to test the base plugin.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
import math
import pytest
from planet_alignment.config.bunch_parser import BunchParser
from planet_alignment.data.system_data import SystemData
from planet_alignment.plugins.base import BasePlugin
from planet_alignment.test import constants


@pytest.fixture(scope='module')
def fix_base():
    return BasePlugin()


@pytest.fixture(scope='module')
def fix_sd_a():
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    it = iter(sd)
    planet_a = it.next()
    return planet_a


@pytest.fixture(scope='module')
def fix_sd_b():
    config_file = constants.TEST_SYSTEM_YAML
    data = BunchParser().parse(config_file)
    sd = SystemData(data)
    it = iter(sd)
    it.next()
    planet_b = it.next()
    return planet_b


def test_get_alignment_delta_degrees(fix_base):
    assert fix_base.get_alignment_delta_degrees() == constants.TEST_DEFAULT_ALIGNMENT_DELTA_DEGREES


def test_set_alignment_delta_degrees(fix_base):
    fix_base.set_alignment_delta_degrees(1)
    assert fix_base.get_alignment_delta_degrees() == float(1)


def test_calculate_alignment_angle_radians_0(fix_base, fix_sd_a):
    angle_rad = fix_base.calculate_alignment_angle_radians(fix_sd_a, 0)
    assert angle_rad == float(0)


def test_calculate_alignment_angle_radians_10(fix_base, fix_sd_a):
    angle_rad = fix_base.calculate_alignment_angle_radians(fix_sd_a, 10)
    assert angle_rad == float(math.pi)


def test_calculate_alignment_angle_radians_20(fix_base, fix_sd_a):
    angle_rad = fix_base.calculate_alignment_angle_radians(fix_sd_a, 20)
    assert angle_rad == float(2 * math.pi)


def test_are_angles_aligned_a0_a0(fix_base, fix_sd_a):
    angle_rad_a = fix_base.calculate_alignment_angle_radians(fix_sd_a, 0)
    assert fix_base.are_angles_aligned(angle_rad_a, angle_rad_a)


def test_are_angles_aligned_a0_b0(fix_base, fix_sd_a, fix_sd_b):
    angle_rad_a = fix_base.calculate_alignment_angle_radians(fix_sd_a, 0)
    angle_rad_b = fix_base.calculate_alignment_angle_radians(fix_sd_b, 0)
    assert fix_base.are_angles_aligned(angle_rad_a, angle_rad_b)


def test_are_angles_aligned_a10_b10(fix_base, fix_sd_a, fix_sd_b):
    angle_rad_a = fix_base.calculate_alignment_angle_radians(fix_sd_a, 10)
    angle_rad_b = fix_base.calculate_alignment_angle_radians(fix_sd_b, 10)
    assert not fix_base.are_angles_aligned(angle_rad_a, angle_rad_b)


def test_are_planets_aligned_a0_a0(fix_base, fix_sd_a):
    assert fix_base.are_planets_aligned(fix_sd_a, fix_sd_a, 0)


def test_are_planets_aligned_a0_b0(fix_base, fix_sd_a, fix_sd_b):
    assert fix_base.are_planets_aligned(fix_sd_a, fix_sd_b, 0)


def test_are_planets_aligned_a10_b10(fix_base, fix_sd_a, fix_sd_b):
    assert not fix_base.are_planets_aligned(fix_sd_a, fix_sd_b, 10)
