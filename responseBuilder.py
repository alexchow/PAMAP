import flask

from werkzeug.datastructures import ImmutableMultiDict
import dataStore

__author__ = 'alexander'

PROTOCOL_ACTIVITIES = [0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 16, 17, 24]

class ResponseBuilder:
    def __init__(self, query_args):
        """
        @type query_args : werkzeug.datastructures.ImmutableMultiDict
        """

        self.window_interval = query_args.get('windowInterval', 500)
        self.sets_per_activity = 1

    def build(self):
        store = dataStore.DataStore()
        """
        :rtype : dict of (int, dict of (int, [ ]))
        :return: A dict of activity ID to dict of session ID to list of samples
        """
        response = { }
        """" :type : dict of (int, dict of (int, [ ])) """

        for activity_id in PROTOCOL_ACTIVITIES:
            sessions = store.randomRawSamples(activity_id, self.window_interval, self.sets_per_activity)
            response[activity_id] = sessions

        return response
