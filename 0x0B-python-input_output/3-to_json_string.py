#!/usr/bin/python3


"""Module with funtion that converts string to it
JSON representation.
"""

import json


def to_json_string(my_obj):
    """Function that gives JSON rep of
    a string object

    Arg
    obj (my_obj): String object to give json rep

    """
    rep = json.dumps(my_obj)
    return (rep)
