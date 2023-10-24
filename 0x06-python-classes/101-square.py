#!/usr/bin/python3
"""defines a class square."""


class Square:
    """class square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a the  Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """takes size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """takes position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """finding area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Printing out the square with symbol #."""
        if self.__size == 0:
            print()
            return
        for d in range(self.__position[1]):
            print()
        for d in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
