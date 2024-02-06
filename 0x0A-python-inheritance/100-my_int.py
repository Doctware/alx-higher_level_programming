#!/usr/bin/python3
""" A cladd MyIint thats inherit from int """


class MyInt(int):
    """ The class my_int """

    def __ne__(self, value):
        """
        operator not equal to
        """
        return super().__eq__(value)

    def __eq__(self, value):
        """
        == operator
        """
        return super().__ne__(value)
