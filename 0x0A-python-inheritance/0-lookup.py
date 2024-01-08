#!/usr/bin/python3
""" this function returns the list of availble attributes
    and method of an object """


def lookup(obj):
    """ returns a list object """
    return dir(obj)
