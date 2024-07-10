#!/usr/bin/python3
"""
Time for an interview!
"""
import requests
import sys


if __name__ == "__main__":
    # Get the repository and owner from command-line arguments
    repository = sys.argv[1]
    owner = sys.argv[2]

    # GitHub API URL to fetch commits
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    # Send GET request to GitHub API
    response = requests.get(url)

    # Parse the JSON response
    commits = response.json()

    # Print the 10 most recent commits
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
