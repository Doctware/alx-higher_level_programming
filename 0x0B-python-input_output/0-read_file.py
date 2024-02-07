#!/usr/bin/python3
""" Function read_file thats read a text file (UTF-8)
    and print it to stdout """


def read_file(filename=""):
    """
    read text file (UTF-8)
    and print to stdout
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
