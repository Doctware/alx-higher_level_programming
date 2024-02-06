#!/usr/bin/python3
""" function that returns True or False """


def is_same_class(obj, a_class):
    """
    Check if objet is exacly an instance of the
    specified class if Yes return True Else return False
    """
    return type(obj) is a_class
