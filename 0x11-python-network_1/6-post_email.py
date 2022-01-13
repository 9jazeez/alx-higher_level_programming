#!/usr/bin/python3
""" A module that takes url as input and displays
the request id on stdout using requests library """

if __name__ == "__main__":
	import requests
	import sys

	value = sys.argv[1]
	email = {'email': sys.argv[2]}

	url = requests.post(value, data=email)
	print("Your email is: {}".format(url.text))
