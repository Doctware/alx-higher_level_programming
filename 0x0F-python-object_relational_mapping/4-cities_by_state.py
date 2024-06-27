#!/usr/bin/python3
""" this module contains a function thats list all cities in the
    given database """
import MySQLdb
import sys


def cities_by_state(username, password, database):
    """ this function connect to the given database
        the print cities by name """

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # creating cursor OBJ
    cur = db.cursor()

    # executing SQL query
    query = """ SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """
    cur.execute(query)

    # getting the feched stuff

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:]

    cities_by_state(username, password, database)
