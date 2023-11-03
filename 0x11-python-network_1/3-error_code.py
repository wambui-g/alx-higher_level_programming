#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and displays the body of the response
"""
import urllib.request
import urllib.error
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(f'Response body: {body}')
except urllib.error.HTTPError as e:
    print(f'Error code: {e.code}')
except urllib.error.URLError as e:
    print(f'Error occurred: {e.reason}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
