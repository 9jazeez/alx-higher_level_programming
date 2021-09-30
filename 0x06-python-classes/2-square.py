#!/usr/bin/python3


""" A Module containing a simple square class"""


class Square:
    """ An empty class that defines
    a square class"""
    def __init__(self, size=0):
        """ The class init method.

        Args:
        attr1 (size): A private instance attribute for the size

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
