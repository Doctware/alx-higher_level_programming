#!/usr/bin/python3
""" this module filtering name by state state """
import MySQLdb
import sys


def my_filter_state(username, password, database, state_n):
    """
        this function display the arsument passed
        to a script
    """

    # connecting to mySQL
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # creating cursor obj
    cur = db.cursor()

    # Executing sql quary
    quary = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(quary, (state_n,))

    # geting the row
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    databace = sys.argv[3]
    state_n = sys.argv[4]

    my_filter_state(username, password, databace, state_n)
