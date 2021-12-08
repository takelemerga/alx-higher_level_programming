#!/usr/bin/python3

'''deine class square'''


class Square:
    '''constractor'''

    def __init__(self, __size=0):
        self.__size = __size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("__size must be an integer")
        elif value < 0:
            raise ValueError("__size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)
