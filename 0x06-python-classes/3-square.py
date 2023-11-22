#!/usr/bin/python3
""" A class square that defines a square by:
    (base on 2-square.py) """


class Square:
    """ define init method """

    def __init__(self, size):
        """
        Inisialized size as the size of the square

        parameters:

        size (int): the size o the square

        Verify size if it is int else raise TypeError

        Check size if it is < 0 else raise ValueError

        """

        try:
            self.__size = size
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
        finally:
            pass

    """
    Defining a public instance method thas returns
    the current ssquare area
    """

    def area(self):

        """
        computing area of square

        Returning area of square
        """

        return self.__size ** 2
