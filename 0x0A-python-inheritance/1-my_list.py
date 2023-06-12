#!/usr/bin/python3

"""The function for my_list class"""


class MyList(list):
    """ a class MyList that inherits from list"""
    pass

    def print_sorted(self):
        """Prints the list in sorted (ascending sort)"""
        print(sorted(self))
