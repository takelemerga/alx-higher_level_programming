#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    lst = list(a_dictionary.keys())
    for j in range(len(lst)):
        if a_dictionary[lst[j]] == value:
            del a_dictionary[lst[j]]
    return (a_dictionary)
