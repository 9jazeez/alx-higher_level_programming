#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i == j:
            pass
        else:
            print("{}{}".format(i, j), end = "")
            print("{}".format("," if i != 8 else " "), end = " ")
print("\n")
