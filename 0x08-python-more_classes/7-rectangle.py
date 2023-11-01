#!/usr/bin/python3
"""this defines a the class ofrectangle"""


class Rectangle:
    """represents a class ofrectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """insantiatiny the rectangle class
        Args:
            width: width of the rectangle
            height: height of rectang
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width attribute"""
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
        """height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rea of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """shows diagram of rectangle which stands for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for col in range(self.__height):
            for ro in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if col < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """returns string form of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints particular message when any object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
