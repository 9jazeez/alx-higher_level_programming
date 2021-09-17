#!/usr/bin/python3


def uniq_add(my_list=[]):
    c = 0
    set1 = set(my_list)
    for i in set1:
        c += i
    return (c)
