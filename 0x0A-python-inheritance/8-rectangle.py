#!/usr/bin/python3
"""takes the class of the baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this a class that defines rectangle with the BaseGeometry
    class
    """
    def __init__(self, width, height):
        """
        this intializes the instance rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
