#!/usr/bin/python3
"""
this script fetches the given URL
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
