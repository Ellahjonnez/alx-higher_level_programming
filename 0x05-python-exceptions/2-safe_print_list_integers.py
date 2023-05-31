#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ a function that prints the first x elements
    of a list and only integers. """

    my_num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            my_num += 1
        except (TypeError, ValueError):
            continue
    print()
    return my_num
