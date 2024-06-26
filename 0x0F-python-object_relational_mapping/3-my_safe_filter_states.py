#!/usr/bin/python3
""" thid module contanis a function that
    connect tp mtSQL to perform crude """


import MySQLdb
import sys


def my_safe_filter_state(username, password, database, state_n):
    """ this function allow it module takes an argument
        and print it also save it from SQL injections
    """
    # connecting to MySQL DB
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # create cursor OBJ
    cur = db.cursor()

    # Executing sql query
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (state_n,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # closing process
    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database, state_n = sys.argv[1:]

    my_safe_filter_state(username, password, database, state_n)
