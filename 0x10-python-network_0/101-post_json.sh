#!/bin/bash
# script that sends JSON POST request to URL passed as the first arg
# and displays the body of the response.
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
