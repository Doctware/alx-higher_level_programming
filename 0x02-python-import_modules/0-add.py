#!/usr/bin/python3
if __name__ == "__main__":
    """ print sum of 1 abd 2"""
    add = __import__('add_0').add

    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
