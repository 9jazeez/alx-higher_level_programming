#!/usr/bin/python3
""" A module that takes url as input and displays
the request id on stdout """

if __name__ == "__main__":
	import urllib.request
	import sys

	value = sys.argv[1]

	url = urllib.request.Request(value)
	with urllib.request.urlopen(url) as request_http:
		content = request_http.read()

	print(request_http.info()['X-Request-Id'])
