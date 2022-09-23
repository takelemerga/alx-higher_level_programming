#!/usr/bin/python3
""" python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


def mystatus():
    """check fetched status"""
    result = requests.get("https://intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(result.text)))
    print("\t- content: {}".format(result.text))


if __name__ == "__main__":
    mystatus()
