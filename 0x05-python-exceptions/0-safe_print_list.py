#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:

        a = 0
        for i in my_list:
            if x <= a:
                break
            print(i, end='')
            a += 1
        print()
        return (a)

    except:
        print()
        return (a)
