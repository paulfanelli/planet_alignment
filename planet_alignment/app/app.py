"""
.. module:: app
   :platform: linux
   :synopsis: The module containing the planet alignment application.

.. moduleauthor:: Paul Fanelli <paul.fanelli@gmail.com>

.. modulecreated:: 6/27/15

"""
from zope.interface import implements
from planet_alignment.app.interface import IApp


class App(object):
    implements(IApp)

    def __init__(self, system_data, plugins, time):
        self._system_data = system_data
        self._plugins = plugins
        self._time = time
