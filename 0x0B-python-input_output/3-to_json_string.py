#!/usr/bin/python3
""" Importing JSON """
import json

""" A function that returns the JSON representation of
    an object (string) """


def to_json_string(my_obj):
    """
    return the JSON obj str
    """
    return json.dumps(my_obj)
