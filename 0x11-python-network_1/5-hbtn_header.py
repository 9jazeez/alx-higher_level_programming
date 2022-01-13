#!/usr/bin/python3
""" A module that takes url as input and displays
the request id on stdout using requests library """

if __name__ == "__main__":
	import requests
	import sys

	value = sys.argv[1]

	url = requests.get(value)
	print(url.headers['X-Request-Id'])
