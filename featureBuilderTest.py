import unittest
from dataStore import DataStore
from featureBuilder import RAW_FEATURES, FeatureBuilder
from responseBuilder import PROTOCOL_ACTIVITIES
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
            raw_data = { activity_id: DataStore().randomRawSamples(activity_id, 500, 3) for activity_id in PROTOCOL_ACTIVITIES[2:5]}
            handAccXFeature = FeatureBuilder().rawFeature(raw_data, "handAccX")
            self.assertEqual(len(handAccXFeature['Standing']), 1500)

    def testBuildAllFeatures(self):
        with start.harApp.test_request_context(""):
            start.set_app_db()
            raw_data = { activity_id: DataStore().randomRawSamples(activity_id, 500, 3) for activity_id in PROTOCOL_ACTIVITIES[2:5]}
            all_features = FeatureBuilder().buildAllRawFeatures(raw_data)
            count = len(all_features)
