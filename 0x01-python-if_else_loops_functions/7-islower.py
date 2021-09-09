#!/usr/bin/python3
def islower(c):
    a = True
    c = ord(c)
    if c >= 90 and c <= 122:
        a = True
    else:
        a = False
    return (a)
