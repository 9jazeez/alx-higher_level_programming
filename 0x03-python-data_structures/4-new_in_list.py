#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        nList = my_list[0:]
    else:
        nList = my_list[0:]
        nList[idx] = element
    return (nList)
