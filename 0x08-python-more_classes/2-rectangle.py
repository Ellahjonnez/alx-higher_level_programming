#!/usr/bin/python3

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
        """ The method that returns the value of the height
        Returns:
            the rectangle height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ This defines the height
        Args:
            value: height
        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ This method calculates the Rectangle area
        Returns:
            the rectangle area
        """

        return self.width * self.height

    def perimeter(self):
        """ The method calculates the Rectangle perimeter
        Returns:
            the rectangle perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)
