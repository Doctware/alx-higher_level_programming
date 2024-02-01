#!/usr/bin/python3
""" A class Rectangle that defines rectangle
    by (by base on 7-rectangle.py)"""


class Rectangle:
    """
    defining public class attribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        inisializing init method parameter

        width and height

        public class attribute number_of_instances
        will be incresing during each new instance
        """
        self.width = width
        self.height height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getting the width

        Returnig it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting width

        check if width is int, if no
        raise TypeError with geiven message
        """

        try:
            if not isinstance(value, int):
                raise TypeError("width must be am ineget")
            elif value < 0:
                raise ValueError("width must >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """
        getting height

        returning it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        seting height

        if height is int if not ratse
        TypeError with the given exception message

        check if height < 0 raise exception maessage
        """

        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must >= 0 ")
            else:
                sefl.__height = height
