#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    """ Replace the element in the specified position """

    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
