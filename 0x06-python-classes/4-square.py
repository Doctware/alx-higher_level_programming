#!/usr/bin/python3
""" A class square that defines by
    (base on 3-square) """


class Square:
    """ Define init method """

    def __init__(self, size=0):
        """
        Inisialize a new insatance of a square class

        parameter:

        size (int): size of square

        Make check on size if it is int else raise TypeError

        Also check if size is >= 0 else raise ValueError

        Then fianlly pass
        """

        self.size = size

    @property
    def size(self):
        """
        Getter method to retrive the size of the square

        Returns:
        int : size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):

        """
        Setter method to retrieve the size of the square

        size (int): size of square

        Make check on size if it is int else raise TypeError

        Also check if size is >= 0 else raise ValueError

        Then fianlly pass
        """

        try:
            self.__size = value
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
        finally:
            pass

    """
    define Publlic method thats return curren square area """

    def area(self):

        """
        calculate the area of current square

        return the area of square
        """

        return self.__size ** 2
