#!/usr/bin/python3
""" function thats add new attribute if possible """


def add_attribute(obj, name, value):
    """ add new attribute if posible """

    if hasattr(obj, "__dict__") and not hasattr(obj, name):
        setattr(obj, name, vale)
    else:
        raise TypeError("can't add new attribute")
