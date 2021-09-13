#!/usr/bin/python3
i = list(map(chr, range(ord('A'), ord('Z') + 1)))
print(*i[0::], sep="")
