#!/usr/bin/python3


"""Module for load_from_json_file """


def load_from_json_file(filename):
    """Function to load from a json file """

    with open(filename, 'r') as f:
        return (json.load(f))
