#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    a = []
    for i in range(len(matrix)):
        a.append([])
    for n, m in enumerate(matrix):
        a[n] = matrix[n][:]
    for y, i in enumerate(a):
        for x, ii in enumerate(a[y]):
            a[y][x] = ii * ii

    return (a)
