#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf-8'))
