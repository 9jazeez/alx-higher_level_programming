#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif str(argv[2]) not in ("-", "*", "+", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        d = argv[2]
        if d == "+":
            c = add(a, b)
        elif d == "-":
            c = sub(a, b)
        elif d == "*":
            c = mul(a, b)
        else:
            c = div(a, b)
        print("{} {} {} = {}".format(a, d, b, c))


