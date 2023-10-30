#!/usr/bin/python3
"""thios defines a class for a rectangle"""


class Rectangle:
    """ a class for the rectangle"""

    def __init__(self, width=0, height=0):
        """this initialises the recta class
        Args:
            width: the width of rectangle
            height:the height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """takes width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """takes the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """a diagram of rectangle for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for ro in range(self.__width):
            for col in range(self.__height):
                rect += "#"
            if col < self.__height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self):
        """string form of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a particular message when
        every object is deleted
        """
        print("Bye rectangle...")
