#!/usr/bin/python3
for i in range(90,64,-1):
    if i % 2 == 0:
        a = chr(i).lower()
    else:
        a = chr(i)
    print(a,end = "")
