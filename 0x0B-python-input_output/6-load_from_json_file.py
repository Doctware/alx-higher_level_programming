#!/usr/bin/python3
""" importing JSON """
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Parameters:
        filename (str): Name of the JSON file to load the object from.

    Returns:
        object: Python object created from the JSON file.

    """
    with open(filename, 'r') as file:
        return json.load(file)
