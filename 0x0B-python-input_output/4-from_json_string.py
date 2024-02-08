#!/usr/bin/python3
""" importing JSON """
import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Parameters:
        my_str (str): A JSON string representing a Python object.

    Returns:
        object: Python object represented by the JSON string.

    """
    return json.loads(my_str)
