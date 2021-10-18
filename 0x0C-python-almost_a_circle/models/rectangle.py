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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    
    @property
    def height(self):
        """A getter """
        return (self.__height)
    
    @height.setter
    def height(self, height):
        """A setter """ 
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
    
    @property
    def y(self):
        """A getter """
        return (self.__y)
    
    @y.setter
    def y(self, y):
        """A setter """ 
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
    
    @property
    def x(self):
        """A getter """
        return (self.__x)
    
    @x.setter
    def x(self, x):
        """A setter """ 
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns area"""
        ar = self.__width * self.height
        return (ar)
    
    def display(self):
        """Display method"""
        for i in range(self.__x):
            print()
        for i in range(self.height):
            print("{} {}".format(" " * self.__y, "#" * self.width))

    def __str__(self):
        """Overriding the __str__"""
        id_str = " (" + str(self.id) + ")"
        a = " " +  str(self.__x) + "/"
        b = str(self.__y) + " "
        c = str(self.__width) + "/"
        d = str(self.__height)

        return ("[Retangle]"  + id_str + a + b + c + d)

