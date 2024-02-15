#!/usr/bin/python3
""" 1-main """

from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10, '$100')
    print(r2.id)
    print("width = {} and height = {} while x = {}".format(r2.width, r2.height, r2.x))

    r3 = Rectangle(10, 2, 0, 0)
    print(r3.id)
