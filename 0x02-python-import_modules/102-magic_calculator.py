#!/usr/bin/python3i

def magic_calculation(a, b):
    """A magic calculator
    Arg:
    a first
    b second

    Return:
    result if function"""

    a = 0
    b = ('add', 'sub')

    from magic_calculation_102 import add, sub

    while a < 94:
        c = add(a, b)
        for i in range(38, 90):
            print(i)
            a = a + 5
    return (a)
