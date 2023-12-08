#!/usr/bin/python3
"""A Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    from requests.exceptions import JSONDecodeError
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) == 2 else ""}

    try:
        response = requests.post(url, data=data).json()
        if response:
            print(f"[{response.get('id')}] {response.get('name')}")
        else:
            print("No result")
    except JSONDecodeError:
        print("Not a valid JSON")
