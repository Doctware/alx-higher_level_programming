#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    """ print sorted dictionary """

    if a_dictionary is None:
        print("Input dictionary is None.")
        return

    if not isinstance(a_dictionary, dict):
        print("Input is not a dictionary.")
        return

    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
