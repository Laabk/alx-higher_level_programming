#!/usr/bin/python3
"""definning a clasfor a rectangle"""


class Rectangle:
    """a class that stands for rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the rec class
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """puts width"""
        return self.__width

    @width.setter
    def width(self, value):
        """puts width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return val for the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """reutur val for perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
