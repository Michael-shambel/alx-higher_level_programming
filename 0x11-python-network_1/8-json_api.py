#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    value = {"q": letter} if len(letter) == 1 else {"q": ""}

    req = requests.post(url, data=value)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")

