#!/usr/bin/python3
def no_c(my_string):

    """ remove letter C & c """

    new_string = ""

    for char in my_string:
        if char != 'C' and char != 'c':
            new_string += char
        
    return new_string
