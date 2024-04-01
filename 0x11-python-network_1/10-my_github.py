#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    resp = requests.get(url, auth=(username, password))
    data = resp.json()
    if 'id' in data:
        print(data['id'])
    else:
        print(None)
