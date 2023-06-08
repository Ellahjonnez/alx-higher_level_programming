#!/usr/bin/python3

""" A module that defines a rectangle class """


class Rectangle:
    """ The Rectangle that defines empty class rectangle """

    def __init__(self, width=0, height=0):
        """ To initializes the instance

        Args:
            width: the rectangle width
            height: the rectangle height

        """
        self._width = width
        self._height = height

    @property """ To set the property of the width """
    def width(self):
        """ To the property of the width

        Returns:
            the rectangle width

        """
        return self._width

    @width.setter """ To define the width """
    def width(self, value):
        """ To define the width

        Args:
            value: width

        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property """ To set the property of the height """
    def height(self):
        """ The property of the height

        Returns:
            the rectangle height

        """
        return self._height

    @height.setter """ To define the heights """
    def height(self, value):
        """ Defines the height

        Args:
            value: the height

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
