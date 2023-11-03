#!/usr/bin/python3
"""
 sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(f'Value of X-Request-Id: {x_request_id}')
        else:
            print('X-Request-Id header not found in the response.')
except urllib.error.URLError as e:
    print(f'Error occurred: {e.reason}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
