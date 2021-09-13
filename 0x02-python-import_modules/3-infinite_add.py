#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("0")

    elif len(argv) > 1:
        c = 0
        for a, i in enumerate(argv):
            if a == 0:
                pass
            else:
                c = c + int(i)
        print("{}".format(c))
