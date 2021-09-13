#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as re
    names = dir(re)
    for name in names:
        if name[1] == "_":
            pass
        else:
            print(name)
