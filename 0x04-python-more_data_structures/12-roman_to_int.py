#!/usr/bin/python3
def roman_to_int(roman_string):

    """ Convert roman numeral to an inteher """

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0

    for i in range(len(roman_string)):
        current_val = roman_numerals[roman_string[i]]

        if  i < len(roman_string) - 1 and roman_numerals[roman_string[i + 1]] > current_val:
            result -= current_val
        else:
            result += current_val

    return result
