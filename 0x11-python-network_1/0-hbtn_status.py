#!/usr/bin/python3
""" this module contains a code that feches the given URL """
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as res:
        result = res.read()
        print("Body response:")
        print(f'\t- type: {type(result)}')
        print(f'\t- content: {result}')
        print(f'\t- utf-8 content: {result.decode("utf-8")}')
