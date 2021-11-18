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
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value


    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
