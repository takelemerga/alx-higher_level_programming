#!/usr/bin/python3
"""sends request to url and display a value of X-Request-Id variable"""
import urllib.request
import sys


def display():
    """display value"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header["X-Request-Id"])


if __name__ == "__main__":
    display()
