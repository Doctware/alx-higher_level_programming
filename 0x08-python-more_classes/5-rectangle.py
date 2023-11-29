#!/usr/bin/python3
""" A rectangle class thats defines a rectangle by
    (base on 4-rectangle.py) """


class Rectangle:
    """ define init method """

    def __init__(self, width=0, height=0):
        """
        Initialize the init method parameter

        Parameter:

        width: the class width
        height: the class height

        """
        self.width = width
        self.height = height

    """ defining private instance attr. width Getter """

    @property
    def width(self):
        """
        Get the value of width

        Returnuing it
        """
        return self.__width

    """ defining private instance attr. width Setter """

    @width.setter
    def width(self, value):
        """
        Set new value to width

        check if value is an integer. else no raise TypeError
        check if value is < 0. if so raise ValueError
        """
        try:
            self.__width = value
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
        finally:
            pass

    """ define private instance atribute. height Getter """

    @property
    def height(self):
        """
        Get the value of width

        Returning it
        """
        return self.__height

    """ define private instanse attr. height Setter """

    @height.setter
    def height(self, value):
        """
        Set new value to height

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

    """ define public instance method thats returns
        the area of Rectangle """

    def area(self):
        """
        compute the area of rectangle

        Returning it
        """
        return self.__width * self.__height

    """ define public method thats returns
        the perimeter of rectangle """

    def perimeter(self):
        """
        Compute the perimeter of rectangle

        Retrning it
        """
        return 2 * (self.__width + self.__height) \
            if self.__width == 0 or self.__height == 0 else 0

    """ define __str__ method that print rectangle with character "#" """

    def __str__(self):
        """
        print rectangle with "#"

        if width or height == 0 print an empty string
        """

        if self.__width == 0 or self.__height:
            return ""

        result = ""
        for _ in range(self.__height):
            result += "#" * self.__width + '\n'
        return result.rstrip()

    """ definr __repr__ method thats returns the pycode of str """

    def __repr__(self):
        """
        print the pycode of str """

        return f"Rectangle({self.__width}, {self.__height})"

    """ define class method """

    @classmethod
    def crate_from_repr(cls, rpre_str):
        """
        Use eval() to create a new instance from
        the string representation
        """
        eval(repr_str)

    """ defining __del__ to destroy Recatngle class """
    def __del__(self):
        """
        Destroiyng Rectangle
        """
        print("By rectangle...")
