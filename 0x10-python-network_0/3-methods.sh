#!/bin/bash
# take in a URL the display the HTTP methods the server accept
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-
