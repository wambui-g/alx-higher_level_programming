#!/usr/bin/python3
"""
 script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad requests

    data = response.json()
    print("Body response:")
    print(f"\t- type: {data['type']}")
    print(f"\t- content: {data['content']}")
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error occurred: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Request Exception occurred: {err}")
