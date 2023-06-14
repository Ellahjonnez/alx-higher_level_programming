#!/usr/bin/python3

"""Student to JSON with filter"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """A class Student that defines a student by:
        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """If attrs is a list of strings, only attribute
          names contained in this list must be retrieved.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
