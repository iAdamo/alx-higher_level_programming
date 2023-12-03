#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | awk '/Allow:/ {gsub(/Allow: /, ""); print}'
