import unittest
import flask
from start import harApp
import start

__author__ = 'alexander'

from flask import Flask, request


class FlaskTester(unittest.TestCase):
    def setUp(self):
        start.harApp.config['TESTING'] = True
        start.harApp.config['DATABASE'] = 'test.db'
        self.app = start.harApp

    def test_get_context(self):
        with self.app.test_request_context("/data?windowInterval=5000"):
            assert flask.request.path == '/data'
            assert flask.request.args['windowInterval'] == '5000'

    def test_get(self):
        with self.app.test_client() as c:
            resp = c.get("/data")

if __name__ == '__main__':
    unittest.main()
