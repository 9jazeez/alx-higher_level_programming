#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")

    elif len(argv) > 1:
        print("{} argument{}:".format((len(argv) - 1), "" if len(argv) == 2
                                      else "s"))
        for a, i in enumerate(argv):
            if a == 0:
                pass
            else:
                print("{}: {}".format(a, i))
