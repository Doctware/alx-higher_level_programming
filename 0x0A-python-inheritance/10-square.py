#!/usr/bin/python3
""" A class Square thats Inherits from Rectangle
    (9-rectangle.py) """


""" importing from 9-rectangle.py """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size):
        """
        Insialize and validate from integer_validator
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        area is being implemented
        """
        return self.__size ** 2
