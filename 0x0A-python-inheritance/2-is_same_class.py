#!/usr/bin/python3

""" A function thats return True if the object
    is an insance of the specific class; else False """


def is_same_class(obj, a_class):
    """
    return True if obj is exacly an insatanse
    of the provided class

    else return False
    """
    return type(obj) is a_class
