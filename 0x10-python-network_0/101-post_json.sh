#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, with the contents of a file passed as the second argument as the body of the request, and displays the body of the response.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
