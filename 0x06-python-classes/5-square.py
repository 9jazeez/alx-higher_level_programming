#!/u-sr/bin/python3


""" This Module contains a square class with differnt methods
Methods like Area and Display
"""


class Square:
    """ An empty class that defines
    a square class"""

    @property
    def size(self):
        """ A getter used to get private attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ A setter for setting the private attribute.

        Args:
        attr1 (size): Private instance attribute

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        """ The init of the class with size atribute"""
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("{}".format(self.__size * "#"))
