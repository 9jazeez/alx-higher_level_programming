#!/bin/bash
#using curl to send a POST of a JSON file content 
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
