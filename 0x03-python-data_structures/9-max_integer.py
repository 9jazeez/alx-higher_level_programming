#!/usr/bin/python3


def max_integer(my_list=[]):
    """Checks max integer

    Args:
    list

    Return:
    Noone, max integer"""
    if len(my_list) == 0:
        return (None)
    i = 0
    while i < len(my_list) - 1:
        max_int = 0
        for a in my_list:
            if a >= my_list[i]:
                if a > max_int:
                    max_int = a
        i += 1
    return (max_int)
