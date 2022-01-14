#!/usr/bin/python3
""" This module uses requests and sys to send http request
and also deal with the error codes. """

if __name__ = "__main__":
	import requests
	import sys

	req = requests.get(sys.argv[1])
	if req.status_code >= 400:
		print("Error code: {}".format(req.status_code))
	else:
		print(req.text)
