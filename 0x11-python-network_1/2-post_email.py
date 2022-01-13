#!/usr/bin/python3
""" Post an email to the server using urllib """

if __name__ == "__main__":
	import urllib.request
	import sys

	value_url = sys.argv[1]
	email = urllib.parse.urlencode({'email': sys.argv[2]})
	email = email.encode('ascii')

	with urllib.request.urlopen(value_url, email) as request_http:

		content = request_http.read()

	print("Your email is: {}".format(content.decode('utf-8')))
