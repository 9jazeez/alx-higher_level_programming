#!/usr/bin/python3
def fizzbuzz():
    for i in range(0,101):
        if i % 3 == 0:
            a = "Fizz"
        elif i % 5 == 0:
            a = "Buzz"
        elif i %  3 == 0 and i % 5 == 0:
            a = "FizzBuzz"
        else:
            a = i
        print(a, end = " ")
