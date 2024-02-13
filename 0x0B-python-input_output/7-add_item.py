#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


""" this script add items to a list """


def add_items_to_list(filename, *args):
    """
    function:

    add the given item to a list
    """
    items = load_from_json_file(filename)
    items.extend(args)

    save_to_json_file(items, filename)


arguments = sys.argv[1:]
add_items_to_list("add_item.json", *arguments)
