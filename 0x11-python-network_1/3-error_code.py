#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body
of the response
"""

import urllib.error
import sys
import urllib.request

if __name__ == '__main__':

    url = sys.argv[1]
    rqst = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(rqst) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
