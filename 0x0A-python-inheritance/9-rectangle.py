#!/usr/bin/python3
""" A class BaseGeometry (based on 5-base_geometry) """


class BaseGeometry:
    """ A class base on 5-base_geometry """

    def area(self):
        """
        return the area of rectangle
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


""" A class Rectangle that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """ def __init__ method """

    def __init__(self, width, height):
        """
        Inisializing width and height

        then

        Validating from integer validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    """ public method area thats return multiplied value """
    def area(self):
        """ return width * height """
        return self.__width * self.__height

    """ def __str__ """

    def __str__(self):
        """
        return reperesentation of a string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
