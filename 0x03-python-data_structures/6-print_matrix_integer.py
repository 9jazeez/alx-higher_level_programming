#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Print matrix

    Elements in rows"""
    if len(matrix) == 0:
        print("")
    else:
        for i in matrix:
            j = 0
            for a in i:
                print("{}{}".format(a, " " if j < len(i) - 1 else ""), end="")
                j += 1
            print()
