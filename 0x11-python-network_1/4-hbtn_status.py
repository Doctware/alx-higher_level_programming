#!/usr/bin/python3
"""
this script fetches the given URL
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    print("Body response")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
