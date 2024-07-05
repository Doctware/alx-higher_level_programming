#!/bin/bash
# take in a URL sends a post rquest to the passed url then display it body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
