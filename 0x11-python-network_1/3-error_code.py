#!/usr/bin/python3
""" Using urllib error exceptions """

if __name__ == "__main__":
	import urllib.request
	import sys

	try:
		value_url = sys.argv[1]
		url = urllib.request.Request(value_url)
		with urllib.request.urlopen(value_url) as request_http:

			content = request_http.read()

	except urllib.error.URLError as e:
		if hasattr(e, 'code'):
			print("Error code: ", e.code)
		elif hasattr(e, 'reason'):
			print("Reason: ", e.reason)
	else:
		print(content.decode('utf-8'))
