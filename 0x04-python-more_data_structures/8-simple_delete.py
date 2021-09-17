#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    dict1 = a_dictionary
    a = dict1.keys()
    if key not in a:
        return (dict1)
    else:
        del(dict1[key])
        return (dict1)
