#!/usr/bin/python3
for ch in range(ord('Z'), ord('A') - 1, -1):
    char = chr(ch)
    if ch % 2 == 0:
        char = char.lower()
    else:
        char = char.upper()
    print("{}".format(char), end="")
