#!/usr/bin/python3
"""
this takes URL, sends request to URL and display value of the X-Request-Id"""

import sys
import urllib.request

if __name__ == '__main__':

    url = sys.argv[1]
    rqst = urllib.request.Request(url)
    with urllib.request.urlopen(rqst) as response:
        print(dict(response.headers).get("X-Request-Id"))
