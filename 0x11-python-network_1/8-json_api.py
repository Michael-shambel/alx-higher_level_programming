#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    value = {"q": letter}

    req = requests.post(url, data=value)
    try:
        resp = req.json()
        if isinstance(resp, dict) and 'id' in resp and 'name' in resp:
            print("[{}] {}".format(resp['id'], resp['name']))
        elif resp == {}:
            print("No result")
        else:
            print("Not a valid JSON")
    except ValueError:
        print("Not a valid JSON")

