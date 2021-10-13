#!/usr/bin/python3


"""Module with funtion that write json to
a file
"""

import json


def save_to_json_file(my_obj, filename):
    """Function that writes into a json
    file

    Arg
    obj (my_str): String object to write to json file
    file (filename): Name of jon file

    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
