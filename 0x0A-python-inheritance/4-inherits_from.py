#!/usr/bin/python3
""" A function thats check if object inherits from
    the given class """


def inherits_from(obj, a_class):
    """
    Work according to the up doc
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
