#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the body of the response
You have to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf8')
            print(body)
    except urllib.error.HTTPError as e:
        er_code = e.code
        print("Error code: {}".format(er_code))
