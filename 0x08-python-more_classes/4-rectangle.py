#!/usr/bin/python3
"""Definning a class of rectangle"""


class Rectangle:
    """a class for rectanglle."""

    def __init__(self, width=0, height=0):
        """an inililiassation
        Args:
            width (int): with of new rectangle.
            height (int): height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the width in rec"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """earea of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """eperimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for d in range(self.__height):
            [rect.append('#') for a in range(self.__width)]
            if d != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """the string form in the Rectangle."""
        ret = "Rectangle(" + str(self.__width)
        ret += ", " + str(self.__height) + ")"
        return (ret)
