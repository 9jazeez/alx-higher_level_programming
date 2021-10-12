#!/usr/bin/python3


"""A module that contains a python function that returns to
the terminal (std-in) a list of all the available attributes
and methods in an object given to it.

"""


def lookup(obj):
    """This function takes in an object
    and returns a list of it attributes
    and methods

    Args:
    obj (obj): Obj to check

    Return: List of attr and mthds

    """
    return (dir(obj))
