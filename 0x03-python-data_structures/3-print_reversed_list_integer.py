#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    """ Print the integer of a list in reverse """
    if my_list:
        for item in reversed(my_list):
            print("{:d}".format(item), end="\n")
