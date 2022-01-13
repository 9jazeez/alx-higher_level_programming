#!/usr/bin/python3
"""A module that connects to a website using urllib"""

if __name__ == "__main__":
	import urllib.request

	url = urllib.request.Request("https://intranet.hbtn.io/status")
	with urllib.request.urlopen(url) as request_http:
		content = request_http.read()

	print("Body response:")
	print("\t- type: {}".format(type(content)))
	print("\t- content: {}".format(content))
	print("\t- utf8 content: {}".format(content.decode('utf-8')))

