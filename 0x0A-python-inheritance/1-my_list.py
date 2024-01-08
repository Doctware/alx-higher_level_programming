#!/usr/bin/python3
""" A class my list that inherits from list
"""


class MyList(list):

    """
    public method thats print the list
    but sorted (ascending sor)
    """

    def print_sorted(self):
        print(sorted(self))
