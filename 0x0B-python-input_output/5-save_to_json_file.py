#!/usr/bin/python3
""" importing JSON """
import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a text file using JSON representation.

    Parameters:
        my_obj (object): Python object to be saved.
        filename (str): Name of the file to save the object to.

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
