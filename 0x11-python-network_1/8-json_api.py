#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
import sys

if len(sys.argv) < 2:
    q = ""
else:
    q = sys.argv[1]

data = {'q': q}

try:
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    response.raise_for_status()  # Raise HTTPError for bad requests

    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error occurred: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Request Exception occurred: {err}")
