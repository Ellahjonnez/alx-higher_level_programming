#!/usr/bin/python3

"""A class MyList that inherits from list"""


class MyList(list):
    """The Class that inherits from list"""
    pass

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
