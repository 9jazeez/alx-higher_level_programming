#!/bin/bash
#Use curl to be silent if there is a response error
curl -sf $1 -X GET 
