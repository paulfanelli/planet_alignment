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

    def run(self):
        result_retval = []

        for plugin_path in self._plugins:
            plugin_inst = self._plugins.get_plugin_instance_by_path(plugin_path)
            plugin_name = self._plugins.get_plugin_name_by_path(plugin_path)

            plugin_str = ''
            unique_aligned_list = []

            for x in self._system_data:

                aligned_list = []
                for y in self._system_data:

                    # don't compare the planets to themselves
                    if x.name == y.name:
                        continue

                    try:
                        result = plugin_inst.are_planets_aligned(x, y, self._time)
                        if result:
                            if x.name not in aligned_list:
                                aligned_list.append(x.name)
                            aligned_list.append(y.name)
                            aligned_list.sort()
                    except AttributeError as ae:
                        print("ERROR: {}: {}".format(plugin_path, ae))
                    except Exception as e:
                        print("ERROR: Unknown error {}".format(e))

                if aligned_list:
                    if aligned_list not in unique_aligned_list:
                        unique_aligned_list.append(aligned_list)

                        plugin_str += plugin_name + ': '
                        aligned_str = ', '.join(*unique_aligned_list)
                        plugin_str += aligned_str + '\n'

            if plugin_str:
                result_retval.append(plugin_str)

        return result_retval

    def print_results(self, results):
        print('\n')
        for line in results:
            print(line)
        return self
