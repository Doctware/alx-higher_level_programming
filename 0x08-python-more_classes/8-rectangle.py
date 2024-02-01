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
