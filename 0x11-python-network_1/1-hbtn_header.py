#!/usr/bin/python3
""" this python script takes in a url send a rquest to the url
    then dispaly the value of the X-Request-id foound on it """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        x_request_id = dict(headers).get("X-Request-Id")
        print(x_request_id)
