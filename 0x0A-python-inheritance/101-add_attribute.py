#!/usr/bin/python3
""" A function add_new attribute tha add
     new attribute if the object can have new """


def add_attribute(obj, attr, value):
    """
    add new attr to an object if posible
    """
    if hasattr(obj, '__dict__') or isinstance(obj, list) or \
            isinstance(obj, dict) or isinstance(obj, set):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
