#!/usr/bin/python3
""" A class Square thats defines a square by:
    (base on 1-square.py) """


class Square:
    """ Define an init method """

    def __init__(self, size=0):

        """
        Inisializing size the size of square

        parameters:

        size (int): the size of the square

        Verify if size is a intger if so raise TypeError with exception
        message: "type must be an integer

        Also check if size is less than 0 if so raise ValueError
        with exception message: size must be >= 0

        """
        try:
            self.__size = size

            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
        finally:
            pass
