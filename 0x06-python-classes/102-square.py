#!/usr/bin/python3
"""classes"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """Instantiation"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def __lt__(self, other):
        return self.__size * self.__size < other.__size * other.__size

    def __le__(self, other):
        return self.__size * self.__size <= other.__size * other.__size

    def __eq__(self, other):
        return self.__size * self.__size == other.__size * other.__size

    def __ne__(self, other):
        return self.__size * self.__size != other.__size * other.__size

    def __gt__(self, other):
        return self.__size * self.__size > other.__size * other.__size

    def __ge__(self, other):
        return self.__size * self.__size >= other.__size * other.__size
