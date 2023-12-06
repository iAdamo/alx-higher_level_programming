#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
