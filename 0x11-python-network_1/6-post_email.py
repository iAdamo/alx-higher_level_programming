#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body of
the response.

Usage: ./6-post_email.py <url> <email address>
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <url> <email address>", file=sys.stderr)
        exit(1)

    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    response = requests.post(url, data=data)
    print(response.text)
