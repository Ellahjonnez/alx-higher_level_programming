#!/usr/bin/python3

""" a class MyList that inherits from list"""


class MyList(list):
    """ The Class that inherits from list"""

    def print_sorted(self):
            """ The that prints the list,
        but sorted in ascending
        """

        sorted_list = sorted(self)
        print(sorted_list)
