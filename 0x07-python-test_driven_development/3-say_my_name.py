#!/usr/bin/python3

"""This module contains a function that prints
the first and last name given to it.

"""


def say_my_name(first_name, last_name=""):
    """A function that prints first
    and last name

    """
    try:
        if not isinstance(first_name, str):
            raise TypeError('first_name must be a string')
        elif not isinstance(last_name, str):
            raise TypeError('last_name must be a string')
        else:
            print("My name is {} {}".format(first_name, last_name))
    except Exception as err:
        print(err)
