#!/usr/bin/python3
"""
 script that takes in a URL, sends a request to the URL and displays the body of the response
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

    print(f'Response body: {response.text}')
    if response.status_code >= 400:
        print(f'Error code: {response.status_code}')
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error occurred: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Request Exception occurred: {err}")
