#!/usr/bin/python3
""" 3-main """

from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print("the area of rectangle is [{}] and the vale of y is [{}] while it id is [{}]".format(r2.area(), r2.y, r2.id))

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area(), r3.id)
