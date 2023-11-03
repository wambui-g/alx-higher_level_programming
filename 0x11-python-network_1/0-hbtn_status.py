#!/usr/bin/python3
"""script that fetches fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("- Body response:")
        print("\t- type:", type(body))
        print("\t- content (UTF-8):")
        print(body.decode("utf-8"))
except urllib.error.URLError as e:
    print("Error occurred:", e)
