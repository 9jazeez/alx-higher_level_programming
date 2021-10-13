#!/usr/bin/python3

"""
Module contains function that append after a str

"""


def append_after(filename="", search_string="", new_string=""):
    """Function that insert after new string

    Args:
    file (filename): Name of file
    str (search_string): que string
    str (new_string): new string to add

    """

    with open(filename, 'r') as f:
        data = f.readlines()

    out = ""
    for line in data:
        out = out + line
        if search_string in line:
            out = out + new_string

    with open(filename, 'w') as f:
        f.write(out)
