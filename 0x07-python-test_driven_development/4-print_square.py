#!/usr/bin/python3

"""This Module contains a function print_square
that print a square using # based on the given size

"""


def print_square(size):
    """Function that prints a square using the length
    called size.

    Args:
    int (size): Size of the square

    Return: Print square using #

    """
    try:
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0 or isinstance(size, float):
            raise ValueError('size must be >= 0')
        elif size == 0:
            pass
        else:
            for i in range(size):
                print("{}".format("#" * size))
    except Exception as err:
        print(err)
