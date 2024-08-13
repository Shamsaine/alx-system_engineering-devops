#!/usr/bin/env bash

# Check if a commit message is provided as an argument
if [ -z "$1" ]; then
  commit_message="added newfiles"
else
  commit_message="$1"
fi

# Add, commit, and push changes
git add .
git commit -m "$commit_message"
git push
