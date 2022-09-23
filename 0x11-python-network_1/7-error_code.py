#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
body of the response using requests
"""
import requests
from sys import argv


def error():
    """
    takes in a URL, sends a request to the URL and displays the
    body of the response using requests
    """
    url = argv[1]
    result = requests.get(url)
    if result.status_code >= 400:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)


if __name__ == "__main__":
    error()
