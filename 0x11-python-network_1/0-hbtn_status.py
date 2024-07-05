#!/usr/bin/python3
""" this module contains a code that feches the given URL """
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    result = res.read()


if __name__ == "__main__":
    print("Body response:")
    print(f'\t- type:" {type(result)}')
    print(f'\t- content: {result}')
    print(f'\t- utf-8 content: {result.decode("utf-8")}')
