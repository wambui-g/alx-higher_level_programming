#!/bin/bash
# using curl to send a request to url and displays the size of the response
curl -sL "$1" | grep 'Content-Length:' | cut -d' ' -f2
