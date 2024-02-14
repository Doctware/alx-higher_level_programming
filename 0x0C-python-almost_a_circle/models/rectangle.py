#!/usr/bin/python3i
"""
This module contans a class Rectangle thats inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ A class Rectangle thats inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ inisialize the class attribute """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returning the area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        print to stout the insatnce of Rectangle
        """
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        Returning info about rectangle
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height} "
