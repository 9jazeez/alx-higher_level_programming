#!/bin/bash
#using curl with more varaible value to POST
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
