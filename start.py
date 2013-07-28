#!/usr/bin/env python
import sqlite3

import sys

from flask import Flask, send_from_directory, request, g
from datapopulator import DataPopulator
from dbmigrator import DbMigrator
from responseBuilder import ResponseBuilder

# configuration
DATABASE = 'test.db'  # default database file

# harApp: Human Activity Recognition Flask Application
harApp = Flask(__name__, static_folder="static")
""":type : Flask"""

# Set configuration to grab the ALL CAPS variables from this file
harApp.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(harApp.config['DATABASE'])

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

@harApp.route("/")
def hello():
    return "Hello World!"

@harApp.route("/view")
def starterView():
    return harApp.send_from_directory('static/', "view.html")

@harApp.route("/data")
def getData():
    responseBuilder = ResponseBuilder(request.args)
    return ""

@harApp.before_request
def before_request():
    g.db = connect_db()

@harApp.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def usage():
    print "Usage: "
    print "start.py [populatedb] [<db filename>]"
    print "where the <db filename> is the name of the database to use. The populatedb argument populates the database" \
          "with with the PAMAP dataset. Omit it to simply run the Flask web server."

# To populate the DB: python start.py populatedb
if __name__ == "__main__":
    dbFilename = None
    if (len(sys.argv) > 3):
        usage()
        exit()
    if (len(sys.argv) < 2):
        harApp.run()
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
        usage()
        exit()
