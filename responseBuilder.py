import flask

from werkzeug.datastructures import ImmutableMultiDict

__author__ = 'alexander'

class ResponseBuilder:
    def __init__(self, query_args):
        """
        @type query_args : werkzeug.datastructures.ImmutableMultiDict
        """

        window_interval = query_args.get('windowInterval', 500)

    def build(self):
        return ""
