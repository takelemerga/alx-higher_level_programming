#!/usr/bin/python3

"""class defined"""


class Square:

    def __init__(self, __size=0):

        if not isinstance(__size, int):
            raise TypeError("__size must be an integer")
        elif __size < 0:
            raise ValueError("__size must be >= 0")
        self.__size = __size

    def area(self):
        return (self.__size ** 2)
