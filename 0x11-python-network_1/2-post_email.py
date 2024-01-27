#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the
"""

import urllib.parse
import sys
import urllib.request

if __name__ == '__main__':

    url = sys.argv[1]
    valu = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(valu).encode('ascii')

    rqst = urllib.request.Request(url, data)
    with urllib.request.urlopen(rqst) as response:
        print(response.read().decode('utf-8'))
