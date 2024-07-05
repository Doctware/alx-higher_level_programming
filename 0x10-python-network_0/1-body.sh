#!/bin/bash
# take in a URL send a get request to the url and display it body
curl -sfL "$1" -X GET
