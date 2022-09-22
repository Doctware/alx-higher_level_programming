#!/usr/bin/python3
def uppercase(_str):
    for a in _str:
        if 97 <= ord(a) <= 122:
            a = chr(ord(a) - 32)
        print("{}".format(a), end="")
    print("")
