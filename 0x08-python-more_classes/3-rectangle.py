#!/usr/bin/python3
""" A class Rectangle thats defines a rectangle by
    (base on 2-rectanngle.py) """


class Rectangle:
    """ defining init method """

    def __init__(self, width=0, height=0):
        """
        Inisializing the parameter of init method

        Parameter

        width: the widt of the rectangle
        height: the height of the rectangle

        """

        self.width = width
        self.height = height

    """ definig private instance attribute for width. Getter """

    @property
    def width(self):
        """
        Getting width

        Returning it

        """
        return self.__width

    """ defining private attribute for width. Setter """

    @width.setter
    def width(self, value):
        """
        set new value to the width

        check if value ia an integer. else no raise TypeError
        check if alue < 0. if so raise ValueError

        """

        try:
            self.__width = value
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
        finally:
            pass

    """ defining private instance attribute for height. Getter"""

    @property
    def height(self):
        """

        Getting width

        Returning it

        """

        return self.__height

    """ defining private instance attribute """

    @height.setter
    def height(self, value):
        """
        set new value to height

        check if value is an integer. else no raise TypeError
        check if value is < 0. if so raise ValueError

        """
        try:
            self.__height = value
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
        finally:
            pass

    """ defining public method thats return the area of Rectangle """

    def area(self):
        """
        Compute the area of rectangle

        Return it
        """

        return self.__width * self.__height

    """ defifnig public instance method thats
        returns the perimeter of rectangle """

    def perimeter(self):
        """
        compute the perimeter of rectangle

        Returning it

        """

        return 2 * (self.__width + self.__height) \
            if self.__width > 0 and self.__height > 0 else 0

    """ defining __str__ method thats return
        reprecentation of a string """

    def __str__(self):
        """
        compute the reprsentation of a str

        Returning it

        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]

    """ defifng __repr__ method thats returns str representation
        of rectangle for reproduction """

    def __rper__(self):
        """
        compute the reproduction of Rectanngle

        Returning it

        """

        return f"Rectanngle({self.__width}, {self.__height})"
