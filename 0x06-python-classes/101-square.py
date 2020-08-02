#!/usr/bin/python3
"""classes"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        printstr = ""
        if self.__size == 0:
            printstr += "\n"
        else:
            for i in range(self.__position[1]):
                printstr += "\n"
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    printstr += " "
                for l in range(self.__size):
                    printstr += "#"
                printstr += "\n"
        return printstr[:-1]

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for f in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
