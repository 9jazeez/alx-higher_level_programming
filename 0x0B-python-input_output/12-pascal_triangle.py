#!/usr/bin/python3

"""
Module for pascal triangle function

"""


def pascal_triangle(n):
    """A function that genertes a pascal triangle

    Args
    int (n): Size of the pascal triangle

    Returns: A list of lists of integers

    """

    lists = []

    if n <= 0:
        return (lists)

    lists = [[1]]
    aux = []
    for i in range(n - 1):
        aux.append(1)
        for f in range(i):
            aux.append(lists[i][f] + lists[i][f+1])
        aux.append(1)
        auxc = aux[:]
        aux = []
        lists.append(auxc)

    return (lists)
