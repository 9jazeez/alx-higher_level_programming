#!/usr/bin/python3

"""Module contains a function that appends into a file.
If the file contains data it adds the new data to it.

"""


def append_write(filename=" ", text=" "):
    """Function that writes into a file and creates it if
    it doesnt exist.

    Args
    file (filename): File to write into
    str (text): str to write into file

    Return: Number of character written into file

    """

    with open(filename, "a") as f:
        value = f.write(text)
    return (value)
