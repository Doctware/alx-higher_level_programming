#!/usr/bin/python3
def add_attribute(obj, name, value):
    if hasattr(obj, "__dict__") or not hasattr(obj, name):
        setattr(obj, name, vale)
    else:
        TypeError("can't add new attribute")
