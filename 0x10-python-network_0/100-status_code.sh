#!/bin/bash
#using curl to get http status code
curl -s -I -o /div/null -w '%{http_code}' "$1"
