#!/usr/bin/python3
""" A rectangle class thats defines a rectangle by
    (base 1-Rectangle.pt) """


class Rectangle:
    """ Define init method """

    def __init__(self, width=0, height=0):
        """
        Inisialize the parameter if init method

        parameter:

        width: the width of the rectangle
        height: height of the rectangle

        """
        self.width = width
        self.height = height

    """ defining private instance attribute. width Getter """

    @property
    def width(self):
        """
        Getting width the class property

        Returning it

        """

        return self.__width

    """ defining private instance attribute. width Setter """

    @width.setter
    def width(self, value):
        """
        set new value to width

        check if value is an integer. else no raise TypeError
        check if value is >= 0. if not raise Value Error

        """
        try:
            self.__width = value
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
        finally:
            pass

    """ defining private instance attribute. height Getter """

    @property
    def height(self):
        """
        Getting height the class property

        Returning it
        """

        return self.__height

    """ defifning private attribute. height setter """
    @height.setter
    def height(self, value):
        """
        set new value to height

        check if value is an integer. else not raise TypeError
        check if value is < 0. if so raise ValueError

        """
        try:
            self.__height = value
            if not isinstance(value, int):
                raise TypeError("height must be an inhteger")
            elif value < 0:
                raise ValueError("height must be >= 0")
        finally:
            pass

    """ defining public instance are
        thats return the area of the Rectangle """

    def area(self):
        """
        returning the area of Rectangle """

        return self.__width * self.__height

    """ definig the public instance method that returns
        the rectangle perimeter """

    def perimeter(self):
        """
            Returning the perimeter of the rectangle """

        return 2 * (self.__width + self.__height) \
            if self.__width > 0 and self.__height > 0 else 0
