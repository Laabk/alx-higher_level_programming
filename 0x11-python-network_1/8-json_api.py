#!/usr/bin/python3
"""
takes in a letter and sends a POST request to n-webpage
with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':

    lett = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": lett}
    rqst = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        th_response = rqst.json()
        if th_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(th_response.get("id"), th_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
