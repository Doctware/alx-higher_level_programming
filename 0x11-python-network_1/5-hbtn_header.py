#!/usr/bin/python3
"""
this python script takes in a URL
then send a requests to the URL and displays
the value of the variable X-Request-id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    req_id = req.headers.get("X-Request-Id")
    print(req_id)
