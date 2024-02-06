#!/usr/bin/python3
""" A class Rectangle thats inherits from BaseGeometry
    (7-base_geimetry) """


""" importing from 7-base_geometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The class Rectangle """

    def __init__(self, width, height):
        """
        Inisializing costructure parameter
        width and height

        Also width and heigh must be validated from Integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
