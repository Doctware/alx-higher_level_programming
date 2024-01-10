#!/usr/bin/python3
""" function thats add new attribute if possible """


def add_attribute(obj, name, value):
    """ add new attribute if posible """

    if hasattr(obj, "__dict__") or not hasattr(obj, name):
        setattr(obj, name, vale)
    else:
        TypeError("can't add new attribute")
