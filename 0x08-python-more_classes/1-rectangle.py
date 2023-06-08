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
        self.width = width
        self.height = height

    @property
    def width(self):
        """The method that returns the value of the width
        Returns:
            The width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ The method that defines the width
        Args:
            value: the width
        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The method that returns the value of the height
        Returns:
            The height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ The method that defines the height
        Args:
            value: The height
        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
