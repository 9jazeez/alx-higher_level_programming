#!/usr/bin/python3


"""Module with funtion that converts json to it
string representation.
"""

import json


def from_json_string(my_str):
    """Function that gives string rep of
    a json object

    Arg
    obj (my_str): String object to give json rep

    """
    rep = json.loads(my_str)
    return (rep)
