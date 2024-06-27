#!/usr/bin/python3
""" this module contains a function thats filtter by citites """
import MySQLdb
import sys


def filter_cities(username, password, database, state_n):
    """ this function takes states as argument then list all cities on it """

    # connecting to mySQL
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # creating curspr Object
    cur = db.cursor()

    # Executing query
    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id ASC;
    """
    cur.execute(query, (state_n,))

    # fetching the result
    rows = cur.fetchall()

    # printing result
    city = ", ".join(row[1] for row in rows)

    print(city)

    # closing proccess
    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database, state_n = sys.argv[1:]

    filter_cities(username, password, database, state_n)
