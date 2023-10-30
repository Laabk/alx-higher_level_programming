#!/usr/bin/python3
"""a class that defines a Rectangle"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """this initializes the instance

        Args:
            width: rthe rectangle width
            height: the rectangle heiht
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the value of the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """value of the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of rectangle"""

        return self.width * self.height

    def perimeter(self):
        """returns the perimeter rectangle"""

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ returns the rec"""

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for d in range(self.height):
            rectangle += ("#" * self.width)
            rectangle += "\n"

        return rectangle[:-1]
