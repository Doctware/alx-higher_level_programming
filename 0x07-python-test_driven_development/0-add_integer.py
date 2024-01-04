#!/usr/bin/python3
"""
this module has a function thats
add 2 integers

"""


def add_integer(a, b=98):
    """
    function that add two integers

    Parameter: a, b

    check if a and b is an integer or float  if not raise TypeError

    Return: The addition of a  and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an int or float")

    return int(a) + int(b)
