#!/usr/bin/python3
""" A class rectangle that inherit from BaseGeometry (7-base_geometry)
    (based on 8-rectangle.py) """


""" importing from 7-base_geometry.py """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The rectangle class """

    def __init__(self, width, height):
        """
        Inisializing init parameter

        Validate from integer_validator
        """
        self.__width = width
        self.integer_validator("width", width)

        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """
        return area of the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print rectangle disdcription
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
