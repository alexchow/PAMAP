import os
from dataparser import DataParser

__author__ = 'alexander'

import _sqlite3 as lite

class DataPopulator:
    def parseDataAndPersistIntoDb(self, db_filename):

        raw_data_filenames = [
            "PAMAP2_Dataset/Protocol/subject101.dat",
            "PAMAP2_Dataset/Protocol/subject102.dat",
            "PAMAP2_Dataset/Protocol/subject103.dat",
            "PAMAP2_Dataset/Protocol/subject104.dat",
            "PAMAP2_Dataset/Protocol/subject105.dat",
            "PAMAP2_Dataset/Protocol/subject106.dat",
            "PAMAP2_Dataset/Protocol/subject107.dat",
            "PAMAP2_Dataset/Protocol/subject108.dat",
            "PAMAP2_Dataset/Protocol/subject109.dat"
        ]



        for (index, dataFilename) in enumerate(raw_data_filenames):
            dataParser = DataParser()
            dataParser.parseFile(dataFilename)
            self.__persistDataParserIntoDb(db_filename, dataParser, index)

    def __persistDataParserIntoDb(self, db_filename, data_parser, user_number):
        with lite.connect(db_filename) as db_connection:
            for (activity, session_list) in data_parser.sessions.items():
                for session in session_list:
                    self.__persistSessionIntoDb(db_connection, user_number, activity, session)

    def __persistSessionIntoDb(self, db_connection, user_number, activity, session):
        """
        @type user_number int
        @type activity int
        @type session dataParser.Session
        """
        c = db_connection.cursor()
        c.execute("""INSERT INTO sessions VALUES(NULL, ?, ?)""", (activity, user_number));
        session_id = c.lastrowid
        for sample in session.samples:
            c.execute("""INSERT INTO raw_samples VALUES(
            NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                      (session_id,
                      sample.timestamp,
                      sample.hr,
                      sample.hand.accX,
                      sample.hand.accY,
                      sample.hand.accZ,
                      sample.hand.gyrX,
                      sample.hand.gyrY,
                      sample.hand.gyrZ,
                      sample.hand.magX,
                      sample.hand.magY,
                      sample.hand.magZ,
                      sample.chest.accX,
                      sample.chest.accY,
                      sample.chest.accZ,
                      sample.chest.gyrX,
                      sample.chest.gyrY,
                      sample.chest.gyrZ,
                      sample.chest.magX,
                      sample.chest.magY,
                      sample.chest.magZ,
                      sample.ankle.accX,
                      sample.ankle.accY,
                      sample.ankle.accZ,
                      sample.ankle.gyrX,
                      sample.ankle.gyrY,
                      sample.ankle.gyrZ,
                      sample.ankle.magX,
                      sample.ankle.magY,
                      sample.ankle.magZ)
                        );
        db_connection.commit()
