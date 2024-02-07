#!/usr/bin/python3
""" this function write a string to a text file (utf-8)
    and returns the number of character written """


def write_file(filename="", text=""):
    """
    write a string to a text file
    """
    with open("filename", 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
