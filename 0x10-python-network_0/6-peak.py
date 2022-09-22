#!/usr/bin/python3
"""
    define a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
        finds the peak in a list of numbers
    """
    length = len(numbr)
    if length == 0:
        return None
    if length == 1:
        return (numbr[0])
    if length == 2:
        return numbr[0] if numbr[0] >= numbr[1] else numbr[1]
    mid = int(length / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
