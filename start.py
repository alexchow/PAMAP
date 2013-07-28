#!/usr/bin/env python

import sys

from flask import Flask
from datapopulator import DataPopulator
from dbmigrator import DbMigrator

app = Flask(__name__)

starting_migrations = [
    """
        CREATE TABLE sessions (id INTEGER PRIMARY KEY NOT NULL, activity INTEGER, user INTEGER);
    """,
    """
        CREATE TABLE raw_samples (
        id INTEGER PRIMARY KEY NOT NULL,
        session_id INTEGER,
        timestamp REAL,
        heartrate REAL,
        handAccX  REAL,
        handAccY  REAL,
        handAccZ  REAL,
        handGyrX  REAL,
        handGyrY  REAL,
        handGyrZ  REAL,
        handMagX  REAL,
        handMagY  REAL,
        handMagZ  REAL,
        chestAccX  REAL,
        chestAccY  REAL,
        chestAccZ  REAL,
        chestGyrX  REAL,
        chestGyrY  REAL,
        chestGyrZ  REAL,
        chestMagX  REAL,
        chestMagY  REAL,
        chestMagZ  REAL,
        ankleAccX  REAL,
        ankleAccY  REAL,
        ankleAccZ  REAL,
        ankleGyrX  REAL,
        ankleGyrY  REAL,
        ankleGyrZ  REAL,
        ankleMagX  REAL,
        ankleMagY  REAL,
        ankleMagZ  REAL,
        FOREIGN KEY(session_id) REFERENCES sessions(id)
        );
    """
]

@app.route("/")
def hello():
    return "Hello World!"

def usage():
    print "Usage: "
    print "start.py [populatedb] [<db filename>]"
    print "where the <db filename> is the name of the db to use to either run the server or populate the data into"

# To populate the DB: python start.py populatedb
if __name__ == "__main__":
    dbFilename = None
    if (len(sys.argv) > 3):
        usage()
        exit()
    if (len(sys.argv) < 2):
        app.run()
    elif (sys.argv[1] == "populatedb"):
        if len(sys.argv) == 3:
            dbFilename = sys.argv[2]
        else:
            dbFilename = "test.db"
        dataMigrator = DbMigrator(dbFilename)
        dataMigrator.migrate(starting_migrations)
        dataPopulator = DataPopulator()
        dataPopulator.parseDataAndPersistIntoDb(dbFilename)
    else:
        dbFilename = sys.argv[1]
