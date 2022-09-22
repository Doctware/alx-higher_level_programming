#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if numbers % 15 == 0:
            print("Fizzbuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d}".format(numbers), end="")
