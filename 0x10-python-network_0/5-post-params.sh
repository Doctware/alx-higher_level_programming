#!/bin/bash
# take in a URL sends a post rquest to the passed url then display it body
curl -s -X POST -d "email=$email" -d "subject=$subject" "$1"
