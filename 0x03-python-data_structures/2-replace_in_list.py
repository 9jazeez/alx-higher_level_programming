#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        nList = my_list
    else:
        nList = my_list
        nList[idx] = element
    return (nList)
