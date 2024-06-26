#!/usr/bin/python3
""" this Module list out the states in he given databases """
import MySQLdb
import sys


def list_state(username, password, database):
    """ this function connect to the MySQL server to list
        out state in the given database """

    # connecting to database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # Creating cursor object
    cur = db.cursor()

    # Execute the SQL quary to get all state
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Getting the rows from quary result
    rows = cur.fetchall()

    # Printing the rows from quary result
    for row in rows:
        print(row)

    # Closing cursor & and connection
    cur.close()
    db .close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_state(username, password, database)
