#!/usr/bin/python3
""" defifnig function thats print square
"""


def print_square(size):
    """
    print square with character "#"

    size is the lenth of square

    size must be an integer if Not! raise TypeError
    with the given exeption message

    if size is less than 0 raise valueErro
    with the given exception message

    if size is a float and is less than 0 raise ValueError
    with the given exception message
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    
    for _ in range(size):
        print("#" * size)
