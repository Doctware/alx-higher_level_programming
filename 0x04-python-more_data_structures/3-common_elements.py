#!/usr/bin/python3
def common_elements(set_1, set_2):

    """ Return the common element bitween two set """

    for look_1 in set_1:
        for look_2 in set_2:
            if look_1 == look_2:
                result = look_1

        return result
