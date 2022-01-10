#!/bin/bash
#Using curl to get content length of an 
#HTTP respond request

url=$1
curl -Is $url | grep -i Content-Length | awk '{print $2}'
