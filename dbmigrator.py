import os
import sqlite3 as lite

__author__ = 'alexander'

class DbMigrator:
    def __init__(self, filename):
        if filename is None:
            raise Exception("You must specify a filename")
        self.filename = filename
        if os.path.isfile(filename):
            raise Exception("Database filename " + filename + " already exists. Aborting DbMigrator")

        self.filename = filename

    # Migrate the DB to migrations. Migrations should be a map: int -> list<string> where
    # the int is the migration number and each list<string> is a list of migrations.
    # Example:
    #   { 1: ["create TABLE activities(int activityCode, string activityName)",
    #         "CREATE table sessions(int sessionId, int activityCode)"],
    #     2: ["CREATE TABLE sample(int id, int sessionId, int sampleInSession)"] }

    def migrate(self, migrations):
        with lite.connect(self.filename) as db_connection:
            c = db_connection.cursor()
            for migration in migrations:
                c.execute(migration)
            db_connection.commit()
