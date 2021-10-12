#!/usr/bin/python3


"""A module that contains a python function that returns to
the terminal (std-in) True if given obj is a member of specified
class and False if otherwise.

"""


def is_same_class(obj, a_class):
    """This function takes in an object
    and returns True if a memeber of a
    class specified

    Args:
    obj (obj): Obj to check
    obj (a_class): class to check from

    Return: True if a member and False if otherwise

    """
    return (type(obj) == a_class)
