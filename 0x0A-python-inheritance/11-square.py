!/usr/bin/python3

""" a module of class Square that inherit 9-Reactangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines class Square that inherits super class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
