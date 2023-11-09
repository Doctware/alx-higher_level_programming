#!/usr/bin/python3
def best_score(a_dictionary):

    """ Return the biggest integer value """

    if not a_dictionary:
        return None

    max_v = max(a_dictionary, key=a_dictionary.get)

    return max_v
