#!/usr/bin/python3
""" defining function that pribt a text with 2 new lines
    after a gien character """


def text_indentation(text):
    """
    print a text wit 2 lines after the 
    each given character

    text must be a string, if not raise TypeError
    with a given message
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
