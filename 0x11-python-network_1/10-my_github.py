#!/usr/bin/python3
"""
takes the GitHub API to display a GitHub ID based on given credentials
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authe = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    rqst = requests.get("https://api.github.com/user", authe=authe)
    print(rqst.json().get("id"))
