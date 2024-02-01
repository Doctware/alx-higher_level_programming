#!/usr/bin/python3
""" definig a function that say my name
"""


def say_my_name(first_name, last_name):
    """
    print first and last name

    if first and last name not str
    raise TypeError with the given exception message
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(first_name + " " + last_name)
