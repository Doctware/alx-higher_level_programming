#!/usr/bin/python3
""" A class rectangle that defines a rectangle by
    (base on 4-rectangle.py) """


class Rectangle:
    """ def init method """

    def __init__(self, width=0, height=0):
        """
        inisialized the instance varible

        parameter:

        width: the width of rectangle
        height: the height o rectangle
        """
        self.width = width
        self.height = height

    """ method to retrive width: getter """

    @property
    def width(self):
        """
        getting the width

        returning it
        """
        return self.__width

    """ method to set width: setter """

    @width.setter
    def width(self, value):
        """
        set value to width

        check if:

        width is an integer, if not raise TypeError
        width is < 0, if True raise ValueError
        """
        try:
            self.__width = value
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
        finally:
            pass

    """ method to retrieve height: getter """

    @property
    def height(self):
        """
        getting the height

        returning it
        """
        return self.__height

    """ method to set heihgt: setter """

    @height.setter
    def height(self, value):
        """
        set value to height

        check if:

        height is an integer, if Not raise TypeError
        height is < 0, if True raise ValueError
        """
        try:
            self.__height = value
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
        finally:
            pass

    """ public instance method that return the area of rectangle """
    def area(self):
        """
        Rerturning the area of rectangle
        """
        return self.__width * self.__height

    """ public instance method that return the rectangle perimeter """
    def perimeter(self):
        """
        returns the perimeter of rctangle

        check if width or height is 0

        if True perimeter == 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    """ def __str__ method that print the rectangle with character "#" """
    def __str__(self):
        """
        print the rectangle with caracter "#"


        if width or height = return empty sring

        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in self.height])

    """ def __repr__ method that return string representation of
        the rctangle to be able to recreate new instance by using eval() """

    def __repr__(self):
        """
        return representation of str

        """

        return f"Rectangle({self.wigth}, {self.height})"

    """ defining a method __del__ that print message
        when an instance is deleted """
    def __del__(self):
        """
        print a message
        """
        print("Bye rectangle...")
