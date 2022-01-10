#!/bin/bash
#Using curl to get content length of an HTTP response 
curl -Is $1 | grep -i Content-Length | awk '{print $2}'
