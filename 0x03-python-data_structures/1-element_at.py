#!/usr/bin/python3
def element_at(my_list, idx):

    """ Return the element from index 3 """

    if idx < 0 or idx >= len(my_list):
        return None

    return my_list[idx]
