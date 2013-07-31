import unittest
from dataStore import DataStore
import featureBuilder
import responseBuilder
import start

__author__ = 'alexander'

class FeatureBuilderTest(unittest.TestCase):
    def setUp(self):
        self.app = start.harApp
        start.harApp.config['TESTING'] = True
        start.harApp.config['DATABASE'] = 'test.db'

    def testBuildHandAccXFeature(self):
        with start.harApp.test_request_context(""):
            start.set_app_db()
            # raw_data = {(activity_id, 10*activity_id) for activity_id in PROTOCOL_ACTIVITIES}
            raw_data = { activity_id: DataStore().randomRawSamples(activity_id, 500, 3) for activity_id in responseBuilder.PROTOCOL_ACTIVITIES[2:5]}
            handAccXFeature = featureBuilder.FeatureBuilder().rawFeature(raw_data, "handAccX")
            for activity in handAccXFeature:
                self.assertEqual(len(activity['values']), 1500)

    def testBuildAllFeatures(self):
        with start.harApp.test_request_context(""):
            start.set_app_db()
            raw_data = { activity_id: DataStore().randomRawSamples(activity_id, 500, 3) for activity_id in responseBuilder.PROTOCOL_ACTIVITIES[2:5]}
            all_features = featureBuilder.FeatureBuilder().buildRawFeaturesForKeys(raw_data, ['handAccX', 'heartrate', 'chestGyrX'])
            count = len(all_features)

    def testMaximum(self):
        with start.harApp.test_request_context(""):
            start.set_app_db()
            raw_data = { activity_id: DataStore().randomRawSamples(activity_id, 500, 4) for activity_id in responseBuilder.PROTOCOL_ACTIVITIES[5:7]}
            maximums = featureBuilder.FeatureBuilder().maximum(raw_data, 'chestAccY')
            count = len(maximums)

    def testTwoWay(self):
        with start.harApp.test_request_context(""):
            start.set_app_db()
            raw_data = { activity_id: DataStore().randomRawSamples(activity_id, 500, 4) for activity_id in responseBuilder.PROTOCOL_ACTIVITIES[5:7]}
            maxChestAccX = featureBuilder.FeatureBuilder().maximum(raw_data, 'chestAccX')
            maxHandAccX = featureBuilder.FeatureBuilder().maximum(raw_data, 'handAccX')
            twoWay = featureBuilder.FeatureBuilder().twoWayCompare(maxHandAccX, maxChestAccX)
            count = len(twoWay)

    def testDft(self):
        with start.harApp.test_request_context(""):
            start.set_app_db()
            raw_data = {activity_id: DataStore().randomRawSamples(activity_id, 500, 4) for activity_id in
                        responseBuilder.PROTOCOL_ACTIVITIES[5:7]}
            dftResult = [
                {
                    'feature_name': 'dft',
                    'data': featureBuilder.FeatureBuilder().dft(raw_data, 'chestAccX')
                }
                , ]

            print dftResult
