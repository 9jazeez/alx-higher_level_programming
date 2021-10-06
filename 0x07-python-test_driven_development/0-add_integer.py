#!/usr/bin/python3


"""A function that adds two integers or floats
Takes two values a and b.
a and must be an integer or float.


"""


def add_integer(a, b=98):
    """add_integer takes two values and returns there sum.

    Args:
    int (a): first value
    int (b): second value

    Return: sum of a and b
    """
    if isinstance(a, str) or isinstance(a, tuple):
        raise TypeError('a must be an integer')
    elif isinstance(b, str) or isinstance(b, tuple):
        raise TypeError('b must be an integer')
    else:
        c = a + b
    return (c)
