#!/usr/bin/python3
""" A function thats returns
    the copy of a lias """


def copy_list(l):
    """
    create an empty list new_list

    copy the element in l to new_list

    Return new_list
    """
    new_list = []
    new_list = l[:]
    return new_list
