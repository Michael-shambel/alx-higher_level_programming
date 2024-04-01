#!/usr/bin/python3
""" Holberton School staff evaluates candidates applying for
a back-end position with multiple technical challenges"""
import sys
import requests

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'

    req = requests.get(url)
    data = req.json()
    for i in range(10):
        print("{}: {}".format(
            data[i].get("sha"),
            data[i].get("commit").get("author").get("name")))
