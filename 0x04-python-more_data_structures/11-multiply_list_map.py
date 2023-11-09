#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):

    """ Return list with all valkue multiply by number """

    new_list = list(map(lambda m: m * number, my_list))

    return new_list
