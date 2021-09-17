#!/usr/bin/python3


def roman_to_int(roman_string):
    """Roman to Int

    Arg:
    String of roman figure

    Return:
    Int of conversion"""
    if roman_string is None or isinstance(roman_string, str) is False:
        return (0)
    c = 0
    a = 0
    t = 0
    f1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        if i in f1:
            if f1.get(i) > a and a > 0:
                t = f1.get(i) - a
                c -= a
                c += t
            else:
                c += f1.get(i)
            a = f1.get(i)
    return (c)
