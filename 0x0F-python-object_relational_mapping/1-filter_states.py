#!/usr/bin/python3
""" this module contains a function that select state Starting from N """
import MySQLdb
import sys


def filter_state(username, password, database):
    """ this functiom select sates starting from Uletter N """

    # connecting to MySQL server
    db = MySQLdb.connect(

            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # creating cursor object
    cur = db.cursor()

    # executing SQL quary
    cur.execute("SELECT * FROM states WHERE name username, password, databaseLIKE 'N%' ORDER BY id ASC")

    # getting rows
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # closing proccess
    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    filter_state(username, password, database)
