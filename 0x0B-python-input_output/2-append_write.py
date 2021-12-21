#!/usr/bin/python3
"""
Module that contains a function that appends
a string at the end of a tex file
"""


def append_write(filename="", text=""):
    """
    appends string and returns number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as filestreamobject:
        chars = filestreamobject.write(text)
    return (chars)
