#!/usr/bin/python3
""" this function append a string to a text file (utf-8)
    and returns the number of character written """


def append_write(filename="", text=""):
    """
    append a string at the end of text file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.seek(0, 2)
        file.write(text)
        return len(text)
