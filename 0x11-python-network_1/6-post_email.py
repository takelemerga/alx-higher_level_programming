#!/usr/bin/python3
"""
That takes in a URL and an email address, sends a POST request to the
"""

import requests
import sys


def postemail():
    """sends post request"""
    email = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], arg=email)
    print('{}'.format(response.text))


if __name__ == "__main__"":
    postemail()
