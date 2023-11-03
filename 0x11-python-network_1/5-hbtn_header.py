#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad requests

    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(f'Value of X-Request-Id: {x_request_id}')
    else:
        print('X-Request-Id header not found in the response.')
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error occurred: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Request Exception occurred: {err}")
