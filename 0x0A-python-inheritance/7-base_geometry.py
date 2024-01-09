#!/usr/bin/python3
""" A class BaseGeometry (based on 5-base_geometry) """


class BaseGeometry:
    """ A class base on 5-base_geometry """

    def area(self):
        """
        public method area that raises an exception
        """
        raise Exception("area() is not implemented")

    """ public instance method integer validator """

    def integer_validator(self, name, value):
        """
        Validate an integer

        check if:
        value is exacly int, else not raise TypeError
        value < 0, if True graise ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
