#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys

def fetch_github_user_id(username, token):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_data = response.json()
        print(f"Your GitHub user ID is: {user_data.get('id')}")
    else:
        print(f"Failed to fetch user ID. Status code: {response.status_code}")

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    fetch_github_user_id(username, token)
