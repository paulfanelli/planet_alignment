"""
.. module:: base
   :platform: linux
   :synopsis: This is the base plugin module. All other plugins should extend it.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
import math
from zope.interface import implements
from planet_alignment import constants
from planet_alignment.plugins.interface import IPlugin


class BasePlugin(object):
    implements(IPlugin)

    def __init__(self, alignment_delta=constants.DEFAULT_ALIGNMENT_DELTA_DEGREES):
        self.alignment_delta = alignment_delta

    def get_alignment_delta_degrees(self):
        return float(self.alignment_delta)

    def set_alignment_delta_degrees(self, value):
        self.alignment_delta = float(value)

    def calculate_alignment_angle_radians(self, planet_data, time):
        theta = float(planet_data.theta)
        period = float(planet_data.period)
        time = float(time)
        angle = theta + 2 * math.pi * time / period
        assert isinstance(angle, float)
        return angle

    def are_angles_aligned(self, angle_x, angle_y):
        assert isinstance(angle_x, float)
        assert isinstance(angle_y, float)
        # calculate the absolute difference in radians
        # http://blog.lexique-du-net.com/index.php?post/Calculate-the-real-difference-between-two-angles-keeping-the-sign
        # at comment #15
        absdiff = math.pi - abs(math.pi - abs(angle_x - angle_y))
        absdiff_deg = math.degrees(absdiff)
        return absdiff_deg < self.get_alignment_delta_degrees()

    def are_planets_aligned(self, planet_x, planet_y, time):
        angle_x = self.calculate_alignment_angle_radians(planet_x, time)
        angle_y = self.calculate_alignment_angle_radians(planet_y, time)
        return self.are_angles_aligned(angle_x, angle_y)
