#!/usr/bin/python3
#!/usr/bin/python3


"""
Function for add_new_attribute method.
"""


def add_new_attribute(obj, attr_name, attr_value):
    """
    Adds new attribute to an object if it's possible.

    Args:
    - obj: The object to add the attribute to.
    - attr_name (str): The name of the attribute.
    - attr_value: The value of the attribute.

    Raises:
    - TypeError: Can't add new attribute
      >> If the attribute cannot be added.
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
