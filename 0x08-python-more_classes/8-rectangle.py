#!/usr/bin/python3
""" A class Rectangle that defines rectangle
    by (based on 7-rectangle.py)"""


class Rectangle:
    """
    defining public class attribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializing init method parameter

        width and height

        public class attribute number_of_instances
        will be increasing during each new instance
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getting the width

        Returning it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting width

        check if width is int, if no
        raise TypeError with given message
        """

        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must >= 0")
            else:
                self.__width = value
        except TypeError as e:
            print(e)

    @property
    def height(self):
        """
        getting the height of rectangle

        Returning it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting height

        if height is int if not raise
        TypeError with the given exception message

        check if height < 0 raise exception message
        """

        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must >= 0 ")
            else:
                self.__height = value
        except TypeError as e:
            print(e)

    def area(self):
        """
        Getting the area rectangle

        Returning it
        """
        return self.width * self.height

    def perimeter(self):
        """
        getting the perimeter of the rectangle

        But if width and height = 0
        then perimeter will be 0

        Returning it
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        print the rectangle with character "#"

        But if width height == 0
        then return empty str
        """
        if self.width == 0 or self.height == 0:
            return ""
        for _ in range(self.__height):
            print("#" * self.__width)

    def __repr__(self):
        """
        Returning the string representation of rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        deleting a rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rec_1, rec_2):
        """
        Returns the biggest rectangle based on the area

        rec_1 must be an instance of rectangle if not!
        raise TypeError with the given exception message

        rec_2 must be an instance of rectangle if not!
        raise TypeError with the given exception message

        Then return rec1_ if both have the same area
        """
        if not isinstance(rec_1, Rectangle):
            raise TypeError("rec_1 must be an instance of Rectangle")
        if not isinstance(rec_2, Rectangle):
            raise TypeError("rec_2 must be an instance of Rectangle")

        area_rec_1 = rec_1.area()
        area_rec_2 = rec_2.area()

        return rec_1 if area_rec_1 >= area_rec_2 else rec_2
