#!/usr/bin/python3
"""
Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


def search_letter(letter):
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    res = requests.post(url, data=data)

    try:
        json_res = res.json()
        if json_res:
            print(f"[{json_res.get('id')}] {json_res.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("not a valid json")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
        search_letter(letter)
