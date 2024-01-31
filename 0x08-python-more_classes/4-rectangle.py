#!/usr/bin/python3
""" A class rectangle (base on 3-main.py)"""


class Rectangle:
    """
    Defines a rectangle with width and height.

    Attributes:
    - width (int): Width of the rectangle.
    - height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
        - width (int): Width of the rectangle (default is 0).
        - height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
        - int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        - value (int): Width value to be set.

        Raises:
        - TypeError: If width is not an integer.
        - ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
        - int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        - value (int): Height value to be set.

        Raises:
        - TypeError: If height is not an integer.
        - ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        - int: Area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
        - int: Perimeter of the rectangle (0 if width or height is 0).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle for printing.

        Returns:
        - str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return \
                "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of
        the rectangle for recreation using eval().

        Returns:
        - str: String representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
