#!/usr/bin/python3
""" A class MyInt thtat inherit from int """


class MyInt(int):
    """
    class thas inherits from int with inverted
    == and !=
    """

    """ def __eq__ method"""
    def __eq__(self, value):
        """
        overide == operator
        """
        return super().__ne__(value)

    """ def __ne__  method """
    def __ne__(self, value):
        """ overide != operaor """
        return super().__eq__(value)
