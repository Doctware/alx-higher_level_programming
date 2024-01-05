#!/usr/bin/python3
""" A class Rectangle that defines a retangle
    based on 1-rectangle """


class Rectangle:
    """ def init method """

    def __init__(self, width=0, height=0):

        """
        Inisializing an instance variable

        parameter:

        width: the width of the rectangle
        height: the height of the rectangle
        """

        self.width = width
        self.height = height

    """ def private instance attribute width """
    @property
    def width(self):
        """
        getting the value of width

        returning it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the value for width

        Check if:

        width is an integer, if False raise TypeError
        width is < 0, if True raise ValueError
        """
        try:
            self.__width = value
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
        finally:
            pass

        """ def private instance attribute height """
    @property
    def height(self):
        """
        getting the value og height

        returning it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the value of hheight

        Check if:

        height is an integer, if False raise TypeError
        height is < 0, if True raise ValueError
        """
        try:
            self.__height = value
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
        finally:
            pass

    """ defining public instance method Area """
    def area(self):
        """
        return the area of rectangle
        """
        return self.width * self.height

    """ defining public instance perimeter"""
    def perimeter(self):
        """
        return the rectangle perimeter

        if width or height = 0 prerimeter is equal to 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    """ Printing rectangle with character # """

    def __str__(self):
        """
        print rectangle with character  #

        if wiidth or height = 0
        return empty string
        """
        if self.width == 0 or self.height == 0:
            return " "
        return "\n".join(["#" * self.width for _ in range(self.height)])
