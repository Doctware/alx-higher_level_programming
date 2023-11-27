#!/usr/bin/python3
""" A class Rectangle thats defines a rectangle by
    (base on 0-rectangle) """


class Rectangle:
    """ define init method """

    def __init__(self, width=0, height=0):
        """ 
        Inisialized the parameter of the of init method

        parameter:

        width: the width of the rectangle
        height: the height of the rectnagle

        """
        self.width = width
        self.height = height

    """ defining private instance for width. Getter """

    @property
    def width(self):
        """
        getting private instance attribute

        Returning it

        """
        return self.__width

    """ defining setter to set it """

    @width.setter
    def width(self, value):
        """
        setting value to the the width

        check if value is an integer. else not raise Type error
        check  width is < 0, if so rase ValueError

        """
        try:
            self.__width = value
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
        finally:
            pass

    """ defining private instance for height. Getter """

    @property
    def height(self):
        """
        getting private instance attribute 

        Returning it
        """

        return self.__height

    """ defining setter to set it """

    @height.setter
    def height(self, value):
        """
        set a value to the height

        check if value is an integer. else not raise TypeError
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
