import responseBuilder
from singleton import Singleton

__author__ = 'alexander'

RAW_FEATURE_NAMES = {
    'heartrate': 'Heart Rate',
    'handAccX':  'Hand Accel X',
    'handAccY':  'Hand Accel Y',
    'handAccZ':  'Hand Accel Z',
    'handGyrX':  'Hand Gyro X',
    'handGyrY':  'Hand Gyro Y',
    'handGyrZ':  'Hand Gyro Z',
    'handMagX':  'Hand Mag X',
    'handMagY':  'Hand Mag Y',
    'handMagZ':  'Hand Mag Z',
    'chestAccX': 'Chest Accel X',
    'chestAccY': 'Chest Accel Y',
    'chestAccZ': 'Chest Accel Z',
    'chestGyrX': 'Chest Gyro X',
    'chestGyrY': 'Chest Gyro Y',
    'chestGyrZ': 'Chest Gyro Z',
    'chestMagX': 'Chest Mag X',
    'chestMagY': 'Chest Mag Y',
    'chestMagZ': 'Chest Mag Z',
    'ankleAccX': 'Ankle Accel X',
    'ankleAccY': 'Ankle Accel Y',
    'ankleAccZ': 'Ankle Accel Z',
    'ankleGyrX': 'Ankle Gyro X',
    'ankleGyrY': 'Ankle Gyro Y',
    'ankleGyrZ': 'Ankle Gyro Z',
    'ankleMagX': 'Ankle Mag X',
    'ankleMagY': 'Ankle Mag Y',
    'ankleMagZ': 'Ankle Mag Z',
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

    def maximum(self, raw_data, data_key):
        return [
            {
                'key': responseBuilder.ACTIVITY_NAMES[activity_id],
                'values': self.__flat_x([max([row[data_key] for row in window])] for window in window_list)
            }
            for (activity_id, window_list) in raw_data.items()
        ]

    def buildRawFeaturesForKeys(self, raw_data, data_keys):
        """
        :type raw_data : dict of (str, list of list of dict)
        :type data_keys : list of str
        :rtype : list of dict

        :param raw_data : A dict from activity name to list (multiple windows) of list of samples (the db query result)

        :returns: A dictionary with a 'feature_name' property and a 'data' property. The 'data' value is in NV D3 format,
                  that is a JSON object with two (key, value) pairs. The first is the ('key' : 'series name') pair.
                  The second is the ('values' : list of points) pair.
        """
        return [
            {
                'feature_name' : RAW_FEATURE_NAMES[feature],
                'data' : self.rawFeature(raw_data, feature)
            }
            for feature in data_keys
        ]

    def __flatten_list_of_list(self, list_of_list):
        return [elem for sublist in list_of_list for elem in sublist]

    def __auto_x(self, y_values):
        """
        Returns a list of dict of (x, y) where the y values are as given and x just increments
        """
        return [{'x': x, 'y': val} for (x, val) in enumerate(y_values)]

    def __flat_x(self, y_values, icon_size=1600):
        """
        Returns a list of dict of (x, y) where y values are as given and all x values are zero
        """
        return [{'x': 0, 'y': val, 'size': icon_size} for val in y_values]
