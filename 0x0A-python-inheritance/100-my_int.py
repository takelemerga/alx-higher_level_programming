#!/usr/bin/python3
"""a module of class MyInt"""


class MyInt(int):
    """Defines class MyInt that inherits built in int class"""

    def __eq__(self, obj):
        """returns false if two int objects are different"""
        return int(self) != obj

    def __ne__(self, obj):
        """returns true if two int objects are same"""
        return int(self) == obj
