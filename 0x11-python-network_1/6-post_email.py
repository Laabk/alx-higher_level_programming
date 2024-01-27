#!/usr/bin/python3
"""
this Sends a POST request to a given URL with a given email.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    valu = {"email": sys.argv[2]}
    rqst = requests.post(url, data=valu)
    print(rqst.text)
