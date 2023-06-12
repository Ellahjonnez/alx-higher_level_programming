#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    A Function that returns True/False if obj is a type of a_class
    Args:
        obj: The object
        a_class: The class type
    Returns:
        True if object is exactly an instance of the specified class
        False, otherwise
    """
    return type(obj) is a_class
