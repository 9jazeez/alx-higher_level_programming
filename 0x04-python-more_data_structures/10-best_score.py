#!/usr/bin/python3


def best_score(a_dictionary):
    """Get Best Score

    Arg:
    dict

    Return:
    int- Best score"""
    c = 0
    myD = a_dictionary
    if myD is None:
        return (None)
    for i in myD:
        for a in myD:
            if myD.get(a) > myD.get(i):
                if myD.get(a) > c:
                    c = myD.get(a)
    for i in myD:
        if myD.get(i) == c:
            return (i, c, max(myD))
