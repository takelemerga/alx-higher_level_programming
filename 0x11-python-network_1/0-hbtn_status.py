#!/usr/bin/python3
""" python script that fetch url 'https://alx-intranet.hbtn.io/status' """
import urllib.request


def fetch_url():
    """fetch the url"""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))


if __name__ == "__main__":
    fetch_url()
