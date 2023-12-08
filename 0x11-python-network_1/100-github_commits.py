#!/usr/bin/python3
"""A Python script that list 10 commits (from the most recent to oldest) of
the repository
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    commits = requests.get(url).json()
    for i in range(10):
        print(f"{commits[i].get('sha')}: "
              f"{commits[i].get('commit').get('author').get('name')}")
