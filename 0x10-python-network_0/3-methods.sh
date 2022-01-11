#!/bin/bash
#curl syntax to show options allowed
curl -sI $1 -X OPTIONS | grep Allow | awk '{print $2}'
