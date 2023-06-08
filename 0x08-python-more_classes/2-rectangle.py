#!/usr/bin/python3

""" Module that defines a class called Rectangle"""


class Rectangle:

    """ The class that defines the rectangle """

    def __init__(self, width=0, height=0):
        """ Method for initializing the instance
        Args:
            width: the rectangle width
            height: the rectangle height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ This returns the value of the width
        Returns:
            the rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ This defines the width
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
        """ This Method returns the value of the height

        Returns:
            rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """ This method defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ This method returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ This method returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (2 * self.__height)
