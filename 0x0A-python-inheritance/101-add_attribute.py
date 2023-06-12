#!/usr/bin/python3


"""
Module for add_attribute method.
"""


def add_attribute(obj, name, value):
    """
    Function to add new attribute to an object if it's possible.

    Args:
    - obj: Object to add the attribute to.
    - name (str): Name of the attribute.
    - value: Value of the attribute.

    Raises:
    - TypeError: If the attribute cannot be added.
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
