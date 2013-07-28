class Sample(object):
    ### rawInputString form:
    ### timestamp | activityID | hr | IMU hand (17 cols) | IMU chest (17 cols) | IMU ankle (17 cols)

    ### rawInputString Example:
    ### 8.38 0 104 30 2.37223 8.60074 3.51048 2.43954 8.76165 3.35465 -0.0922174 0.0568115 -0.0158445 14.6806 -69.2128
    #           -5.58905 1 0 0 0 31.8125 0.23808 9.80003 -1.68896 0.265304 9.81549 -1.41344 -0.00506495 -0.00678097
    #           -0.00566295 0.47196 -51.0499 43.2903 1 0 0 0 30.3125 9.65918 -1.65569 -0.0997967 9.64689 -1.55576
    #           0.310404 0.00830026 0.00925038 -0.0175803 -61.1888 -38.9599 -58.1438 1 0 0 0


    # Constructs a new sample object by parsing the rawInputString, classifying the activity it the with classification
    # Note, the hr column is ignored. Instead, the heartrate parameter is used instead because the column is often NaN
    # and should adopt its value from a prior row.
    def __init__(self, rawTokens, heartRate):
        if (len(rawTokens) != 54):
            raise Exception("Error, malformed sample. Incorrect number of cells")
        self.rawTokens = rawTokens
        self.timestamp = float(rawTokens[0])
        self.activityId = int(float(rawTokens[1]))
        self.hr = heartRate
        self.hand = Imu(rawTokens[3:20])
        self.chest = Imu(rawTokens[20:37])
        self.ankle = Imu(rawTokens[37:54])

class Imu(object):
    # Parses tokens to produce an Imu instance.
    # tokens must consist have 17 elements. Elements 5-7 and 14-17 are discarded.
    def __init__(self, tokens):
        values = map(float, tokens)
        self.temperature = values[0]
        self.accX = values[1]
        self.accY = values[2]
        self.accZ = values[3]
        # Discard elements 5-7 since they are bad data.
        self.gyrX = values[7]
        self.gyrY = values[8]
        self.gyrZ = values[9]
        self.magX = values[10]
        self.magY = values[11]
        self.magZ = values[12]
        #discard elements 14-17 since they are invalid
