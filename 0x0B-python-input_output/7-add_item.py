#!/usr/bin/python3
""" importing from modules """
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def main():
    """
    Add command-line arguments to a Python list and save them to a file.

    Usage:
        python script_name.py arg1 arg2 ...

    Arguments:
        arg1, arg2, ...: Command-line arguments to be added to the list.

    """
    items = load_from_json_file("add_item.json") if sys.argv[1:] else []

    for arg in sys.argv[1:]:
        items.append(arg)

    save_to_json_file(items, "add_item.json")
