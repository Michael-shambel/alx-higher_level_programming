#!/usr/bin/python3
""" Python script that fetches url"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    rep = urllib.request.urlopen(url)
    body = rep.read().decode('utf8')
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
