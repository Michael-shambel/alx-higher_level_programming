#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL

Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        Request_Id = response.headers.get('X-Request-Id')
        print(Request_Id)
