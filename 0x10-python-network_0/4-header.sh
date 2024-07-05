#!/bin/bash
# take in a url send a get request to it then display the body
curl -s -H "X-School-user-id: 98" "$1"
