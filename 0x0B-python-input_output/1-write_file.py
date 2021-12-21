#!/usr/bin/python3
"""
a module that contains a function that writes
a string to a text file
"""


def write_file(filename="", text=""):
    """
    write to text file and returns the number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as filestreamobject:
        char_num = filestreamobject.write(text)
        return (char_num)
