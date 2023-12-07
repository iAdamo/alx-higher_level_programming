#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print('Body response:')
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
