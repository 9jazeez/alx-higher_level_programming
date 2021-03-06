#!/usr/bin/python3


"""Module for function that opens a file.
File should be UTF8 format"""


def read_file(filename=" "):
    """Function that reads a txt file
    to stdout

    Args
    file (filename): Name of file to read from

    Return : Output on stdout
    """

    with open(filename, 'r') as f:
        read_data = f.read()
    print(read_data, end="")
