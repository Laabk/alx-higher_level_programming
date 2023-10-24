#!/usr/bin/python3
"""defines the class square"""


class Square:
    "the class square"

    def __init__(self, size=0, position=(0, 0)):
        "Initialize a squuare"
        self.size = size
        self.position = position

    @property
    def size(self):
        "the size of the square."
        return self.__size

    @size.setter
    def size(self, value):
        "Setting the size of the square"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        "takes the position of the square"
        return self.__position

    @position.setter
    def position(self, value):
        "Setting position of the square"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        "returns area of the square"
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for d in range(self.__position[1]):
                print()
            for d in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
