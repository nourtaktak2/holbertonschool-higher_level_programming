#!/usr/bin/python3
"""classes"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """Instantiation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
