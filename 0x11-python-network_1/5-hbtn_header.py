#!/usr/bin/python3
"""
this displays the X-Request-Id header variable of a request to a given URL.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    rqst = requests.get(url)
    print(rqst.headers.get("X-Request-Id"))
