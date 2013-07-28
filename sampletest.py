__author__ = 'alexander'

import unittest
from sample import *

class TestSampleParsing(unittest.TestCase):
    def test_basic(self):
        rawString = """1583.91 12 NaN 33.8125 -3.35002 2.82677 1.98172 -3.34551 2.98799 2.25576 -1.44272 0.741315
                        0.224253 26.4945 -36.3523 -24.8126 1 0 0 0 36.1875 0.108742 3.7008 -1.63276 0.0138956 3.49224
                        -1.53608 0.377035 0.305409 -0.0680196 10.2686 -56.4977 -19.8187 1 0 0 0 34.875 2.01233 0.118058
                        -2.23447 1.55843 0.724217 -1.39452 1.53468 -0.650282 1.8661 -53.0936 -2.69607 -18.4615 1 0 0 0"""

        hr = 85.23
        sample = Sample(rawString.split(), hr)
        self.assertEqual(sample.timestamp, 1583.91)
        self.assertEqual(sample.activityId, 12)
        self.assertEqual(sample.hr, hr)
