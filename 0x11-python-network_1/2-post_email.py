#!/usr/bin/python3
"""
this script takes in a url and an email then send a POST request
to the passed URL with the email as a parameter
and dispplay the body of the response (decode in utf-8)
"""
import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
