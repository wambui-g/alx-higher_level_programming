#!/usr/bin/python3
"""
takes URL and email, sends POST request to the passed URL with the email as a parameter, displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email parameter for the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(f'Response body: {body}')
except urllib.error.URLError as e:
    print(f'Error occurred: {e.reason}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
