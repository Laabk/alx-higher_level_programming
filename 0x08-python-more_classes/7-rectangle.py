#!/usr/bin/python3
"""definning a class for the rectangle"""


class Rectangle:
    """a claass for the rectanglle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """this inilises the recta class
        theargs:
            width (int): with of new rectangle.
            height (int): height of new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """the width of rec"""
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
        """height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return a val area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return a val for perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """this prints the form of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        reca = []
        for d in range(self.__height):
            [reca.append(str(self.print_symbol)) for a in range(self.__width)]
            if d != self.__height - 1:
                reca.append("\n")
        return ("".join(reca))

    def __repr__(self):
        """string form for the Rectangle."""
        reca = "Rectangle(" + str(self.__width)
        reca += ", " + str(self.__height) + ")"
        return (reca)

    def __del__(self):
        """Print a message when any deleted Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
