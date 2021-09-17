#!/usr/bin/python3


def search_replace(my_list, search, replace):
    list1 = my_list[0:]
    for a, i in enumerate(list1):
        if i == search:
            list1[a] = replace

    return (list1)
