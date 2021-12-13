#!/usr/bin/python3
"""It is a python code about the class
"""

class Rectangle:
    """Defines the python class Rectangle.
       sets and gets the private instance variables 
    """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle class instance.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and return  the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the created rectagle object.
           raiseError:
                     TypeError or ValueError if any one occured
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the created rectagle object.
           raiseError:
                     TypeError or ValueError if any one occured
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
