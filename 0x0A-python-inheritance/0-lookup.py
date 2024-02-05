#!/usr/bin/python3
""" defining a function thats returns the list
    of available attributes and methos of an object """


def lookup(obj):
    """
    return the list of attributes and and methods of an object
    """
    return dir(obj)
