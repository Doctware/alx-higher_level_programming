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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        this class method write....
        the json string representation of list_objs to file
        """
        if list_objs is None:
            list_objs = []

        cls_name = cls.__name__
        filename = "{}.json".format(cls_name)

        with open(filename, 'w') as file:
            json_data =\
                cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.iwrite(json_data)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of json string representatiopn """
        if json_string is None or json_string is {}:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attribute already set """
        dummy_inst = cls(1, 1)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        
        filename = "{}.json".fromat(cls.__name__)

        if filename is None:
            return []
        else:
            with open(filename, 'r') as file:
                json_data = file.read()
                dictionaries = json.loads(json_data)
                instnaces = [cls.create(**d) for d in dictonaries]
                return instances
