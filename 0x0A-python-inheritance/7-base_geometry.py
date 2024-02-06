#!/usr/bin/python3
""" A class BaseGeometry (base on 5-base_goemetry) """


class BaseGeometry:
    """ definin public method area """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check if value is not an integer
        raise TypeError with the given exception message

        If value is <= 0: raie ValueError
        with the given exception message
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an inte")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
