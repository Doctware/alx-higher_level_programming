#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ print the first x element of a list and all integers """
    try:
        count = 0

        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            count += 1

    except (ValueError, TypeError):
        pass

    except IndexError:
        print("list index out of range")

    return count
