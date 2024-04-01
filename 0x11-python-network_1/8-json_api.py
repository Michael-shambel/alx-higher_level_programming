#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    value = {"q": letter}
    url = 'http://0.0.0.0:5000/search_user'

    req = requests.post(url, data=value)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
