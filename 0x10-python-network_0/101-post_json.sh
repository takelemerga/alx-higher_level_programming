#!/bin/bash
# Script sends a JSON POST request to a URL first argument, displays the body of response
# the script sends a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
