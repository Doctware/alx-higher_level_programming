#!/usr/bin/python3
""" This module contains a class Base """


class Base:
    """ the Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ inisializing init value """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
