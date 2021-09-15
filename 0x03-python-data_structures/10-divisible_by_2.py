#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Get divisible by two

    Arg:
    list

    Return:
    True and False list"""
    check = []
    for i in my_list:
        if i % 2 == 0:
            check.append(True)
        else:
            check.append(False)
    return (check)
