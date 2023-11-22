#!/usr/bin/python3
""" importing math module """
import math
""" the magicClass """


class MagicClass:
    """MagicClass defines a class with magical properties."""

    def __init__(self, radius):
        """
        Initializes a new instance of the MagicClass.

        Parameters:
        - radius: The radius of the magic circle.
                  Must be a number (float or integer).
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magic circle.

        Returns:
        - float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the magic circle.

        Returns:
        - float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
