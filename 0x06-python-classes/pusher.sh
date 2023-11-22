#!/bin/bash
# An Auto pusher

git add $1 # The file to be add
git commit -m "$2" # a commit message in a quote
git push # finally push to the github

echo "---------------------"
echo ""
echo "done!!! :)"
