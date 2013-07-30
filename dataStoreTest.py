import unittest
from dataStore import DataStore
import start

__author__ = 'alexander'

class DataStoreTest(unittest.TestCase):
    def setUp(self):
        self.app = start.harApp
        start.harApp.config['TESTING'] = True
        start.harApp.config['DATABASE'] = 'test.db'

    def testGetRawSamples(self):
        with start.harApp.test_request_context(""):
            # Test request contexts don't automatically call before_request. Set up DB manually.
            start.set_app_db()
            dataStore = DataStore()
            sample_sets = dataStore.randomRawSamples(5, 500, 2)

            self.assertEqual(len(sample_sets), 2, "Number of sets retrieved was not as expected")
            for sample_set in sample_sets:
                self.assertEqual(len(sample_set), 500, "Sample set size was not as expected")

    def testListOfDictInversion(self):
        data = [ {'id': 1, 'name' : 'alice'}, {'id': 2, 'name': 'bob'}, {'id': 4, 'name': 'charlie'}]
        store = DataStore()
        result = store._DataStore__listOfDictToDictOfList(data)
        self.assertEqual(len(result['id']), 3, "Incorrect number of elements in column")
