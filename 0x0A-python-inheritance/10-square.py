#!/usr/bin/python3
"""this function represems a rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """
        initializing the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
