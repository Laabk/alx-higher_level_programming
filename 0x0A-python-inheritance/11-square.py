#!/usr/bin/python3
"""
a function that defines a rectangle subclass Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this func stands for square class"""

    def __init__(self, size):
        """
        initialize the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
