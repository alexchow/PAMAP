import responseBuilder
from singleton import Singleton

__author__ = 'alexander'

RAW_FEATURES = {
    'heartrate': 'heartrate',
    'handAccX': 'Hand Acc X',
    'handAccY': 'Hand Acc Y',
    'handAccZ': 'Hand Acc Z'
}


class FeatureBuilder(Singleton):
    """
    Takes a raw response from the data store and builds a feature from it in the proper form for NV D3 to display.
    """

    def rawFeature(self, raw_data, data_key):
        """
        This "feature" is not really a feature. It just extracts the raw data corresponding to the key data_key
        :type raw_data : dict of (str, list of list of dict)
        :type data_key : str

        :param raw_data : A dict from activity_id to list (multiple windows) of list of samples (the db query result)
        :param data_key : The key to get the data from the list of dict in raw_data

        :rtype : dict of list of list
        :returns: Dict from activity_id to list (multiple windows) of list of values
        """
        return [
            {
                'key': responseBuilder.ACTIVITY_NAMES[activity_id],
                'values': self.__auto_x([row[data_key] for window in window_list for row in window])
            }
            for (activity_id, window_list) in raw_data.items()]


    def buildAllRawFeatures(self, raw_data):
        """
        :type raw_data : dict of (str, list of list of dict)
        :rtype : dict of (str, list of list)

        :param raw_data : A dict from activity name to list (multiple windows) of list of samples (the db query result)

        :returns: a dictionary with key as feature name, value as list of chart series.
                  Each chart series must be in NV D3 format, that is a JSON object with two (key, value) pairs.
                  The first is the ('key' : 'series name') pair.
                  The second is the ('values' : list of points) pair.
        """
        return {RAW_FEATURES[feature]: self.rawFeature(raw_data, feature) for feature in RAW_FEATURES.keys()}

    def __flatten_list_of_list(self, list_of_list):
        return [elem for sublist in list_of_list for elem in sublist]

    def __auto_x(self, y_values):
        """
        Returns a list of dict of (x, y) where the y values are as given and x just increments
        """
        return [{'x': x, 'y': val} for (x, val) in enumerate(y_values)]
