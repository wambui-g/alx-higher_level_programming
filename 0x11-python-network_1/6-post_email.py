#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response
"""
import requests
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise HTTPError for bad requests

    print(f'Response body: {response.text}')
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error occurred: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Request Exception occurred: {err}")
