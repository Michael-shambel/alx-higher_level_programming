#!/usr/bin/python3
""" Python script that fetches url"""
import urllib.request
url = https://alx-intranet.hbtn.io/status
rep = urllib.request.get(url)
print("Body response:")
print("\t- type: {}".format(type(rep)))
print("\t- content: {}".format(rep))
