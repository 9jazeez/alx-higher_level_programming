#!?usr/bin/python3


def multiply_by_2(a_dictionary):
    dict1 = a_dictionary
    dict2 = {}
    for i in dict1:
        dict2[i] = dict1.get(i) * 2

    return (dict2)
