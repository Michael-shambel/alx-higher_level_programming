#!/usr/bin/python3
""" Python script that fetches url"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    rep = requests.get(url)
    body = rep.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
