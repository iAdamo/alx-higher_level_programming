#!/usr/bin/python3
"""A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    if len(sys.argv) != 3:
        print(f"{sys.argv[0]} <username> <password>", file=sys.stderr)
        exit(1)

    url = 'https://api.github.com/user'
    credentials = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    response = requests.get(url, auth=credentials).json()
    print(response.get('id'))
