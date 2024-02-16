#!/usr/bin/python3
""" This module contains a class Base """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returning the json str representation of list_dictonaries
        """
        if list_dictionaries is None or list_dictionaries is {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
