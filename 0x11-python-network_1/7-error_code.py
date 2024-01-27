#!/usr/bin/python3
"""
this takes in a URL, sends a request to the URL and displays the body
of the response."""

import sys
import requests

if __name__ == '__main__':

    url = sys.argv[1]
    rqst = requests.get(url)
    if rqst.status_code >= 400:
        print("Error code: {}".format(rqst.status_code))
    else:
        print(rqst.text)
