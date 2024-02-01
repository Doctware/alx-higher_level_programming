#!/usr/bin/python3
""" creating a function thats adds 2 number
"""


def add_integer(a, b=98):
    """
    Add two integer

    Parameter a and b must be integer or float

    else:

    raise a TypeError with exception message

    Cast a and b into an integer before returning

    Then Returns an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
