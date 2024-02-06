#!/usr/bin/python3
""" A class base geometry (base on 6-base_gemetry) """


class BaseGeometry:
    """ Base geometry class """

    def area(self):
        """
        Raise an exception with the given
        exception message
        """
        raise Exception("area() is not implemened")

    def integer_validator(self, name, value):
        """
        check if is an integer, if not Raise TypeError
        with the given exception

        check if value is <= 0 raise ValueError
        with the given exception message
        """
        if is type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
