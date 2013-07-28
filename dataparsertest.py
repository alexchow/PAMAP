import unittest
from dataparser import DataParser

__author__ = 'alexander'

class TestSampleParsing(unittest.TestCase):
    def testBasicFileParsing(self):
        dataParser = DataParser()
        dataParser.parseFile("PAMAP2_Dataset/Protocol/subject101.dat")