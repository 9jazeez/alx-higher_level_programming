#!/usr/bin/python3

if __name__ == "__main__":
	import requests
	import sys
	
	req = requests.get("https://api.github.com/user", auth=(sys.argv[1],
			    sys.argv[2]))
	print(req.json().get('id'))
