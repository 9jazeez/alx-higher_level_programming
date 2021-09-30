#!/u-sr/bin/python3


""" This module defines a class with it init value
and it area
"""


class Square:
    """ An empty class that defines
    a square class"""

    @property
    def size(self):
        """ A getter property to get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ A setter used to set the size.

        Args:
        value: Int value for the size

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        """The init method for the class

        Args:
        attr1 (size): Private instance attribute size

        """
        self.__size = size

    def area(self):
        """ Return the area of the square"""
        return (self.__size ** 2)
