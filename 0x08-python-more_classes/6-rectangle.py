#!/usr/bin/python3
"""this defines a clas for the rectangle object"""


class Rectangle:
    """a class for the rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """this initialises the rectangle class
        theargs:
            width: stands for the width of rectangle
            height: stands for the height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """takes width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """takes width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """takes height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """takes height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """diagram any rectan that is defined any cre object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for ro in range(self.__width):
            for col in range(self.__heigth):
                reca += "#"
            if col < self.__height - 1:
                reca += "\n"
        return (reca)

    def __repr__(self):
        """returning a string form of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when any object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
