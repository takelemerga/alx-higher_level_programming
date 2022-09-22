#!/bin/bash
# takes in a URL and displays all HTTP methods that  will accepted by the server
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
