#!/usr/bin/python3
"""
represents a class of rectangle from the BaseGeometry class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class for a rectangle that usesthe BaseGeometry
    """

    def __init__(self, width, height):
        """this intializes the new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """this returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """this prints()with the strin() representation of a Rectangle"""
        b_str = "[" + str(self.__class__.__name__) + "] "
        b_str += str(self.__width) + "/" + str(self.__height)
        return (b_str)
