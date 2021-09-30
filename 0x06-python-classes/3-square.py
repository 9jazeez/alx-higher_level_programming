#!/usr/bin/python3

""" This module defines a class with it init value
and it area
"""


class Square:
    """ An empty class that defines
    a square class"""

    def __init__(self, size=0):
        """ The init method with the size
        attritubes.

        Args:
        attr1 (size): A private instamce attribute size

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ A method that returns the area """
        return (self.__size ** 2)
