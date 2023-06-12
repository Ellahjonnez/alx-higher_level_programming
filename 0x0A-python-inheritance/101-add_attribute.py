#!/usr/bin/python3


"""
Module for add_attribute method.
"""


def add_new_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
    - obj: The object to add the attribute to.
    - name (str): The name of the attribute.
    - value: The value of the attribute.

    Raises:
    - TypeError: Can't add new attribute
      >> If the attribute cannot be added.
    """

    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
