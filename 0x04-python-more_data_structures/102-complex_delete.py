#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    dict1 = a_dictionary
    a = dict1.values()
    if value not in a:
        return (dict1)
    else:
        c = []
        for i in dict1:
            if dict1.get(i) == value:
                c.append(i)
        for i in c:
            del(dict1[i])
    return (dict1)
