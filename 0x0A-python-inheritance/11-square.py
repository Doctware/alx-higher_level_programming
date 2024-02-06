#!/usr/bin/python3
""" A class square that inherits from (9-rectangle)
    (base om 10-rectangle) """


""" importing from 9-rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class rectangle """

    def __init__(self, size):
        """
        inisializing
         and
        validating
        """
        self.__size = size

        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        return a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        print a square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
