#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    n = 0

    if len(tuple_a) > len(tuple_b):
        a = tuple_a
        b = tuple_b
    else:
        a = tuple_b
        b = tuple_a

    for i in range(len(a)):
        if i >= len(b):
            c = a[i] + 0
            result.append(c)
        else:
            c = a[i] + b[i]
            result.append(c)
    result2 = tuple(x for x in result)

    return (result2)
