#!/usr/bin/python3
"""
Pascal triangle def.
"""


def pascal_triangle(n):
    """function to make it"""
    if n <= 0:
        return []
    cont = []
    for i in range(n):
        start = [1]
        if cont:
            last = cont[-1]
            start.extend([sum(pair) for pair in zip(last, last[1:])])
            start.append(1)
        cont.append(start)
    return cont
