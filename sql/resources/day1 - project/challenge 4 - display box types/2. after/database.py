#
#
#
"""Helper functions to lightly abstract the interaction with the
database"""

import sqlite3
from data_types import Box


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


def add_box(connection, box):
    try:
        connection.execute("INSERT INTO boxes (name, x, y, z) VALUES (?, ?, ?, ?)", box)
        connection.commit()
        print("\nBox saved successfully!\n")
    except sqlite3.IntegrityError as e:
        print("\nSorry! Could not persist box to database: ", e, "\n")


def get_all_boxes(connection):
    fetched = connection.execute("SELECT * FROM boxes;").fetchall()

    if fetched:
        return [Box(*b) for b in fetched]
