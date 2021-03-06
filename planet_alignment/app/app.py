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
    """This class houses the main application and runs the planet alignment.

    - **parameters** and **types**::

        :param system_data: The system data object containing planet alignment data.
        :param plugins_mgr: The plugins manager object containing a list of plugins.
        :param time: The amount of time to calculate the alignment for.
        :type system_data: SystemData object.
        :type plugins_mgr: PluginsManager object.
        :type time: float
    """
    implements(IApp)

    def __init__(self, system_data, plugins_mgr, time):
        self._system_data = system_data
        self._plugins_mgr = plugins_mgr
        self._time = time

    def run(self):
        """Runs the planet alignment algorithm.

            :return: Returns a list of results, if there are any, else an empty list.
            :rtype: list
        """
        result_retval = []

        for plugin_path in self._plugins_mgr:
            try:
                plugin_inst = self._plugins_mgr.get_plugin_instance_by_path(plugin_path)
                plugin_name = self._plugins_mgr.get_plugin_name_by_path(plugin_path)
            except (KeyError, AttributeError) as e:
                print("WARNING: {}".format(e))
                continue

            plugin_str = ''
            unique_aligned_list = []
            first_entry = True

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

            for unique_aligned_entry in unique_aligned_list:
                if first_entry:
                    first_entry = False
                else:
                    plugin_str += '\n'
                plugin_str += plugin_name + ': ' + ', '.join(unique_aligned_entry)

            if plugin_str:
                result_retval.append(plugin_str)

        return result_retval

    def print_results(self, results):
        """Prints the results from the run of the planet alignment algorithm.

            :param results: List of the results output data.
            :type results: list
            :return: Returns the self reference.
            :rtype: App class.
        """
        for line in results:
            print(line)
        return self
