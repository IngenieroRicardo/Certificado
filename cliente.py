import sys
import requests
import urllib3

urllib3.disable_warnings()

if len(sys.argv)>1:
	response = requests.get(url='https://demo.com/', cert=('cert.pem', 'key.pem'), verify=False)
	print(response.text)
else:
	response = requests.get(url='http://demo.com/')
	print(response.text)