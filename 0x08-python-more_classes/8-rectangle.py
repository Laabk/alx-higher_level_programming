#!/usr/bin/python3
"""this defines the class oddf rectangle"""


class Rectangle:
    """ a class rectangle"""
    instance = 0
    symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing thw class of rectangle
        Args:
            width: width o rectangle
            heigh: height of rectangl
        """
        self.width = width
        self.height = height
        Re.instance += 1

    @property
    def width(self):
        """takes thewidth attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """takes the width attribute"""
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
        """takes height attribute"""
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
        """diagram o rectangle defined for the object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        re = ""
        for col in range(self.__height):
            for ro in range(self.__width):
                try:
                    re += str(self.symbol)
                except Exception:
                    re += type(self).symbol
            if col < self.__height - 1:
                re += "\n"
        return (r)

    def __repr__(self):
        """string form of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when object is deleted"""
        print("Bye rectangle...")
        Re.instance -= 1

    @staticmethod
    def bigger_or_equal(rec, reca):
        if not isinstance(rec, Rectangle):
            raise TypeError("rec isan instance of Rectangle")
        if not isinstance(reca, Rectangle):
            raise TypeError("reca is an instance of Rectangle")
        if rec.area() >= reca.area():
            return rec
        else:
            return reca
