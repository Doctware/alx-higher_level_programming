#!/bin/bash
# take in a URL sends a post rquest to the passed url then display it body
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST -d "email=$email" -d "subject=$subject" "$1"
