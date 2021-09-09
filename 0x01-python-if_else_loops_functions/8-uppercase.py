#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a = ord(i)
        if a > 90:
            a = a - 32
        print("{}".format(chr(a)), end = "")
    print("\n")
