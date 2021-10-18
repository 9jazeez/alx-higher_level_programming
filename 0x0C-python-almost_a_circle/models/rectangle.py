#!/usr/bin/python3


"""
This module containss a rectangle class that
inherits from the base class

"""


from models.base import Base


class Rectangle(Base):
    """Rectangle with width and height.
    Also inherits from class Base

    """

    @property
    def width(self):
        """A getter """
        return (self.__width)

    @width.setter
    def width(self, width):
        """A setter """
        self.__width = width
    
    @property
    def height(self):
        """A getter """
        return (self.__height)
    
    @height.setter
    def height(self, height):
        """A setter """
        self.__height = height
    
    @property
    def y(self):
        """A getter """
        return (self.__y)
    
    @y.setter
    def y(self, y):
        """A setter """
        self.__y = y
    
    @property
    def x(self):
        """A getter """
        return (self.__x)
    
    @x.setter
    def x(self, x):
        """A setter """
        self.__x = x

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

