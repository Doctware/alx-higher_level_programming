#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    
    """ print the first x element of a list and all integers """

    for i in range(x):
        count = 0

        try:
            print("{:d}".format(my_list[i]), end="")
            count += i

        except (ValueError, TypeError):
            pass

    print()
    return count
