#!/usr/bin/python3
""" A class Mylist that inherit from List """


class MyList(list):
    """
    Public instance method print_sorted
    thats prints list, but sorted (ascending sort)

    Assumes all elemet of list is of type int
    """

    def print_sorted(self):
        """
        print sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
