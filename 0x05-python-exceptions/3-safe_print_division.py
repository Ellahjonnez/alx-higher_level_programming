#!/usr/bin/python3

def safe_print_division(a, b):
    """ a function that divides 2 integers
    and prints the result."""

    try:
        div_num = a / b
    except (TypeError, ZeroDivisionError):
        div_num = None
    finally:
        print("Inside result: {}".format(div_num))
    return (div_num)
