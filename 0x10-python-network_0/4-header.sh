#!/bin/bash
# takes in a URL as argument, sends a GET request to URL and displays body of response
# A header variable X-School-User-Id must be sent with the value 98
curl -sH "X-School-User-Id: 98" "$1"
