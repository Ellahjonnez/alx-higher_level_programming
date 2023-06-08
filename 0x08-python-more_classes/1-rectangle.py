#!/usr/bin/python3

""" A module that defines a rectangle class """


class Rectangle:

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property """ To set the property of the width """
    def width(self):
        return self._width

    @width.setter """ To define the width """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property """ To set the property of the height """
    def height(self):
        return self._height

    @height.setter """ To define the heights """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
