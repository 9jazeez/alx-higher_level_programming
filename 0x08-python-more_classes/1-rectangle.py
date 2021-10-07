#!/usr/bin/python3


"""This Module contains a Rectangle function
maker.

"""


class Rectangle:
    """A rectangle is a plane shape with
    with a length and a breadth.
    This class makes rectangles.
    """
    @property
    def width(self):
        """A getter property to get the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """A setter used to set the width

        Args:
        int (width): width

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """A getter property to get the width of the rectangle"""
        return (self.__height)

    @width.setter
    def height(self, value):
        """A setter used to set the width

        Args:
        int (width): width

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """A function or method to instanciate an instance

        Args:
        int (width): width
        int (height): height

        """
        self.__width = width
        self.__height = height
