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
    """This class houses the base plugin. All other plugins should derive from it.

    - **parameters** and **types**::

        :param alignment_delta: The planet alignment delta, defaults to 5 degrees.
        :type alignment_delta: float
    """
    implements(IPlugin)

    def __init__(self, alignment_delta=constants.DEFAULT_ALIGNMENT_DELTA_DEGREES):
        self.alignment_delta = alignment_delta

    def get_alignment_delta_degrees(self):
        """Get the alignment delta.

            :return: Returns the alignment delta.
            :rtype: float
        """
        return float(self.alignment_delta)

    def set_alignment_delta_degrees(self, value):
        """Set the alignment delta.

            :param value: The alignment delta.
            :type results: float
        """
        self.alignment_delta = float(value)

    def calculate_alignment_angle_radians(self, planet_data, time):
        """Calculate the alignment angle in radians.

            :param planet_data: A Bunch object containing planet data.
            :type planet_data: Bunch object.
            :param time: The amount of time to calculate the planet alignment for.
            :type time: float
            :return: Returns the angle in radians.
            :rtype: float
        """
        theta = float(planet_data.theta)
        period = float(planet_data.period)
        time = float(time)
        angle = theta + (2 * math.pi * time / period)
        return angle

    def are_angles_aligned(self, angle_x, angle_y):
        """A boolean determining if the two planet angles are aligned.

            :param angle_x: angle of planet x in radians
            :type angle_x: float
            :param angle_y: angle of planet y in radians
            :type angle_y: float
            :return: Returns True if the angles are aligned, else False.
            :rtype: bool
        """
        assert isinstance(angle_x, float)
        assert isinstance(angle_y, float)
        # calculate the absolute difference in radians
        # http://blog.lexique-du-net.com/index.php?post/Calculate-the-real-difference-between-two-angles-keeping-the-sign
        # at comment #15
        absdiff = math.pi - abs(math.pi - abs(angle_x - angle_y))
        absdiff_deg = math.degrees(absdiff)
        return absdiff_deg < self.get_alignment_delta_degrees()

    def are_planets_aligned(self, planet_x, planet_y, time):
        """A boolean determining if the two planets are aligned.

            :param planet_x: planet x system data as a Bunch object
            :type planet_x: Bunch object
            :param planet_y: planet y system data as a Bunch object
            :type planet_y: Bunch object
            :return: Returns True if the planets are aligned, else False.
            :rtype: bool
        """
        angle_x = self.calculate_alignment_angle_radians(planet_x, time)
        angle_y = self.calculate_alignment_angle_radians(planet_y, time)
        return self.are_angles_aligned(angle_x, angle_y)
