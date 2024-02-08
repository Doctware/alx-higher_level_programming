#!/usr/bin/python3
""" A function thats returns the dictonary discription
    wtih simple data structure """


def class_to_json(obj):
    """
    Convert an object to a dictionary with
    simple data structures for JSON serialization.

    Parameters:
        obj: An instance of a class with attributes that are serializable.

    Returns:
        dict: Dictionary description of the object suitable
        for JSON serialization.

    """
    if not hasattr(obj, '__dict__'):
        return obj

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
        elif value is not None:
            result[key] = class_to_json(value)
    return result
