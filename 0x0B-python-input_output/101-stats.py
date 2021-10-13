#!/usr/bin/python3

"""
Stdin input and comptes metrics task

"""

if __name__ == "__main__":
    import sys

    std_terminal = sys.stdin

    c = 0
    size = 0

    mtr = ['200', '301', '400', '401', '403', '404', '405', '500']
    st = {}

    try:
        for li in std_terminal:
            if c == 10:
                print("File size: {}".format(size))
                for i in sorted(st):
                    print("{}: {}".format(i, st[i]))
                c = 1
            else:
                c = c + 1

            li = li.split()

            try:
                size = size + int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if li[-2] in mtr:
                    if st.get(li[-2], -1) == -1:
                        st[li[-2]] = 1
                    else:
                        st[li[-2]] = st[li[-2]] + 1
            except IndexError:
                pass

        print("File size: {}".format(size))
        for i in sorted(st):
            print("{}: {}".format(i, st[i]))

    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for i in sorted(st):
            print("{}: {}".format(i, st[i]))
        raise
