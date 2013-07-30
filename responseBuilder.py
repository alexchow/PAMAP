import flask

from werkzeug.datastructures import ImmutableMultiDict
from dataStore import DataStore
import featureBuilder

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

        self.window_interval = query_args.get('windowInterval', 200, type=int)
        self.activities = query_args.get('activities', PROTOCOL_ACTIVITIES, type=str)
        data_keys_string = query_args.get('data_keys', type=str)
        if data_keys_string != None:
            self.data_keys = data_keys_string.split(',')
        else :
            self.data_keys = ['handAccX', 'handAccY', 'chestAccX', 'chestAccY', 'ankleGyrX', 'heartrate']

        self.numWindows = query_args.get('numWindows', 3, type=int)

    def build(self):
        """
        :rtype : dict of (int, dict of (int, [ ]))
        :return: A dict of activity ID to dict of session ID to list of samples
        """

        random_raw_data_all_activities = { activity_id: DataStore().randomRawSamples(activity_id, self.window_interval, self.numWindows) for activity_id in self.activities}
        rawFeatures = featureBuilder.FeatureBuilder().buildRawFeaturesForKeys(random_raw_data_all_activities, self.data_keys)
        maximumFeatures = [
            {
                'feature_name': 'Max ' + data_key,
                'data' : featureBuilder.FeatureBuilder().maximum(random_raw_data_all_activities, data_key),
                'plot_type' : 'scatterChart'
            }
            for data_key in self.data_keys
        ]

        # Take union of all the dicts
        return rawFeatures + maximumFeatures
