#!/u-sr/bin/python3


""" Module for A simple Square class that performs few functions"""


class Square:
    """ An empty class that defines
    a square class"""

    @property
    def size(self):
        """A getter for the square class"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ A setter for setting private attribtes

        Args:
        attr1 (size): Private instance attribute

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Second property  with position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """For setting the cordinate of the square

        Args:
        attr1 (value): Value for money

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple integers")

    def __init__(self, size=0):
        """General init value"""
        self.__size = size

    def area(self):
        """Returns Area of Square """
        return (self.__size ** 2)

    def my_print(self):
        """Prints shape of square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("{}".format(self.__size * "#"))
