#!/usr/bin/python3
""" This module uses requests to send an http request
to intranet.hbtn.io """

if __name__ == "__main__":
	import requests 
	value = "https://intranet.hbtn.io/status" 

	url = requests.get(value)
	print("Body response:")
	print("\t- type: {}".format(type(url.text)))
	print("\t- content: {}".format(url.text))
