#!/bin/bash
# take in a URL send a get request to the url and display
# the body of the response
curl -sfL "$1" -X GET
