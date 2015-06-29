"""
.. module:: align1
   :platform: linux
   :synopsis: A python alignment file plugin, derived from the base plugin.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/28/15

"""
from planet_alignment.plugins.base import BasePlugin


class Align2Plugin(BasePlugin):
    def __init__(self):
        super(Align2Plugin, self).__init__(alignment_delta=1)
