#!/usr/bin/python3
""" This module searches from the json api.
 It uses requests and sys to post a value 
to search for from the server users. """

if __name__ == "__main__":
	import requests
	import sys

	search = {'q': ""}
	if len(sys.argv) > 1:
		search['q'] = sys.argv[1]
	req = requests.post("http://0.0.0.0:5000/search_user", data=search)
	if "json" not in req.headers.get('content-type'):
		print("Not a valid JSON")
	else:
		if req.json():
			print("[{}] {}".format(req.json().get('id'),
			      req.json().get('name')))
		else:
			print("No result")
