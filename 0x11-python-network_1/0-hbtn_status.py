#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(html), html, html.decode('utf-8')))
