#!/bin/bash
# take in a URL send request to the url and dispplay the size of the response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
