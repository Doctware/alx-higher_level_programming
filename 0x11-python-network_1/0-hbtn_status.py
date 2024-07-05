#!/usr/bin/python3
""" this module contains a code that feches the given URL """
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as res:
        result = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(result)))
        print("\t- content: {}".format(result))
        print("\t- utf-8 content: {}".format(result.decode("utf-8")))
