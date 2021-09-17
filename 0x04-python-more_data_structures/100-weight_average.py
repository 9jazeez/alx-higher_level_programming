#!/usr/bin/python3


def weight_average(my_list=[]):
    nums = 0
    dens = 0
    for a, b in my_list:
        nums += (a * b)
        dens += b
    return (nums / dens)
