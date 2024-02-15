#!/usr/bin/python3
"""
this module contains A class square thats inherits from `Rectangle`
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ inisializing the attribute oof the class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Reurning information for Square """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
