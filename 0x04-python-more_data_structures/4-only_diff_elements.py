#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    """ Return a set thats is present in only one set """

    present_set = set()

    for elem in set_1:
        if elem not in set_2:
            present_set.add(elem)

    for elem in set_2:
        if elem not in set_1:
            present_set.add(elem)

    return present_set
