#
#
#
"""Helper functions to lightly abstract the interaction with the
database"""

import sqlite3


def create_database_and_tables(filename):
    if not filename:
        filename = ":memory:"

    connection = sqlite3.connect(filename)

    connection.execute("PRAGMA foreign_keys = 1;")
    connection.commit()

    ddl = """
        DROP TABLE IF EXISTS boxes;
        CREATE TABLE boxes (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            x REAL NOT NULL,
            y REAL NOT NULL,
            z REAL NOT NULL,
            CONSTRAINT max_volume CHECK ( x * y * z < 10)
        );
        DROP TABLE IF EXISTS freight;
        CREATE TABLE freight (
            id INTEGER PRIMARY KEY,
            container_id INTEGER NOT NULL,
            box_id INTEGER NOT NULL REFERENCES boxes(id) ON DELETE CASCADE
        );
    """

    connection.executescript(ddl)

    return connection
