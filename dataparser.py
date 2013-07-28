__author__ = 'alexander'

from sample import Sample

class Session:
    def __init__(self):
        self.samples = [ ]

class DataParser:

    def __init__(self):
        # Sessions is a map: activityCode -> List<Session>
        self.sessions = { }

    # Parse a single data file.
    # Parsing proceeds as follows:
    #       Iterate over the rows. Skip rows until a valid activityID is found.
    #       session <- new empty list of samples.
    #       with activityId:
    #           Skip until valid HR.
    #           Consume row, parse as new sample. Add to list.
    #           Go to next row and repeat
    #
    #
    # Returns a set< (classification, list<sample>) >
    def parseFile(self, path):
        with open(path, 'rU') as f:
            currentActivity = None
            currentHr = None
            currentSession = None
            for line in f:
                tokens = line.split()
                assert len(tokens) == 54

                # Skip the line if no current session and cannot adopt activity from row
                if (currentSession == None and not tokens[1].isdigit()):
                    continue


                # Check if activity has changed
                if currentActivity != int(tokens[1]):
                    print "Parsing new activity: " + tokens[1]
                    currentActivity = int(tokens[1])
                    currentSession = self.startNewSession(currentActivity)
                    currentHr = None

                # Skip the line if no current heart rate and cannot adopt hr from row
                if currentHr == None and (tokens[2] == "NaN" or not tokens[2].isdigit()):
                    continue

                # Adopt the current heart rate
                if tokens[2].isdigit(): currentHr = int(tokens[2])
                try:
                    nextSample = Sample(tokens, currentHr)
                    currentSession.samples.append(nextSample)
                except Exception:
                    print "Failed to parse sample. Igoring"


    # Create and return a new session
    def startNewSession(self, activityCode):
        newSession = Session()
        if not self.sessions.has_key(activityCode):
            self.sessions[activityCode] = [ ]

        self.sessions[activityCode].append(newSession)
        return newSession


