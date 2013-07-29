import random
from flask import g
from singleton import Singleton
from start import harApp

__author__ = 'alexander'

# An interface for the sqlite database

class DataStore(Singleton):
    def __query_db(self, query, args=(), one=False):
        """
        Parameters:
        @type query : str
        one - set to True to return just the first of the query result
        """
        cur = g.db.execute(query, args)
        rv = [dict((cur.description[idx][0], value)
                   for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv

    def randomRawSamples(self, activity_id, samples_per_set, num_sets=1):
        """
        :type activity_id : int
        :type samples_per_set : int
        :type num_sets : int

        :rtype: [ (int, [ ] ) ]
        :return: List of tuples of session id and samples. The samples are a randomly chosen contiguous set of samples
                 corresponding to the specified activity id and has num_samples number of elements
        """

        result = []

        while len(result) < num_sets:
            sessions = self.__query_db("SELECT id, user from SESSIONS where activity = ?", (activity_id,))
            """ :type : list of dict of (int, int)"""

            if len(sessions) < 1: continue

            # Choose a random session
            session_id = sessions[random.randint(0, len(sessions)) - 1]['id']
            """ :type : int """

            print "Using random session id: " + str(session_id)

            samples = self.__query_db("SELECT * from raw_samples where session_id = ? order by timestamp", (session_id,))
            """ :type samples : list of dict of (unknown, unknown) """

            if samples is None: continue
            if len(samples) < samples_per_set: continue

            starting_point = random.randint(0, len(samples) - samples_per_set)
            """ :type : int"""

            result.append((session_id, samples[starting_point:starting_point + samples_per_set]))

        return result

