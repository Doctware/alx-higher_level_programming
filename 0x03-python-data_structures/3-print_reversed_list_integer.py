#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    """ Print the integer of a list in reverse """

    for item in reversed(my_list):
        print("{}".format(item))