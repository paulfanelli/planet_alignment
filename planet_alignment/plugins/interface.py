"""
.. module:: interface
   :platform: linux
   :synopsis: An interface to a plugin.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
from zope.interface import Interface


class IPlugin(Interface):
    """An interface to a plugin"""

    def get_alignment_delta_degrees():
        """Return the alignment delta degrees value."""

    def set_alignment_delta_degrees(value):
        """Set the alignment delta degrees value."""

    def calculate_alignment_angle_radians(planet_data, time):
        """Returns the calculated alignment angle"""

    def are_angles_aligned(angle_x, angle_y):
        """Returns True if the two planet angles are considered aligned, else False"""

    def are_planets_aligned(planet_x, planet_y, time):
        """Returns True if the two planets are considered aligned, else False"""
