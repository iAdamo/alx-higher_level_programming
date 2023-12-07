#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the body
of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <url>", file=sys.stderr)
        exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
