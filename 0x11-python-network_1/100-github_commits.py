#!/usr/bin/python3
""" Using requests to get commits from github api"""

if __name__ == "__main__":
	import requests
	import sys

	count = 0
	rep = requests.get("https://api.github.com/repos/"\
		+ sys.argv[2] + '/' + sys.argv[1] + '/commits')
	res = rep.json()
	for i in res:
		if count > 9:
			break
		print(i.get('sha') + ': ', end="")
		print(i.get('commit').get('author').get('name'))
		count += 1
