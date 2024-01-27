#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == '__main__':

    rqst = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(rqst) as response:
        page = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode('utf-8')))
