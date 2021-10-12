#!/usr/bin/python3

"""
module for add_attribute
"""


def add_attribute(obj, key, value):
    """This function adds new attr to an object

    Args:
    obj (obj): Object to add new attr
    attr (key) : atrribute to add
    attr (value): attribute to add

    """

    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(obj, "__slots__") and not hasattr(obj, key):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
