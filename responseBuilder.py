import flask

from werkzeug.datastructures import ImmutableMultiDict
from dataStore import DataStore
from featureBuilder import FeatureBuilder

__author__ = 'alexander'

PROTOCOL_ACTIVITIES = [1, 2, 3, 4, 5, 6, 7, 12, 13, 16, 17, 24]
ACTIVITY_NAMES = {
    1 : 'Lying',
    2 : 'Sitting',
    3 : 'Standing',
    4 : 'Walking',
    5 : 'Running',
    6 : 'Cycling',
    7 : 'Nording Walking',
    9 : 'Watching TV',
    10 : 'Computer Work',
    11 : 'Car Driving',
    12 : 'Ascending Stairs',
    13 : 'Descending Stairs',
    16 : 'Vacuum Cleaning',
    17 : 'Ironing',
    18 : 'Folding Laundry',
    19 : 'House Cleaning',
    20 : 'Soccer',
    24 : 'Jump Rope'
}

class ResponseBuilder:
    def __init__(self, query_args):
        """
        @type query_args : werkzeug.datastructures.ImmutableMultiDict
        """

        self.window_interval = query_args.get('windowInterval', 500)
        self.activities = query_args.get('activities', PROTOCOL_ACTIVITIES)
        self.sets_per_activity = 1

    def build(self):
        """
        :rtype : dict of (int, dict of (int, [ ]))
        :return: A dict of activity ID to dict of session ID to list of samples
        """
        random_raw_data_all_activities = { activity_id: DataStore().randomRawSamples(activity_id, 500, self.sets_per_activity) for activity_id in self.activities}
        return FeatureBuilder().buildAllRawFeatures(random_raw_data_all_activities)
