#!/usr/bin/python3
"""
text identation module:
indents text
useful
"""


def text_indentation(text):
    """prints a text with 2 new lines after some characters. 
       Text must be a string, There should be no space
    at the beginning
    or at the end of each printed line.
    """
    # text is a string, otherwise raise a TypeError
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    txt = text.replace('.', '.\n\n')
    txt = txt.replace('?', '?\n\n')
    txt = txt.replace(':', ':\n\n')

    print("\n".join([line.strip() for line in txt.split("\n")]), end="")
