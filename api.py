import requests
import json

lookup_url = "http://dev.markitondemand.com/Api/v2/lookup/json?input="

def api_scraper(string):
	result=lookup_url + string
	r = requests.get(result)
	print(r.text)
	data = json.loads(r.text)
	return (data)

u =input("Enter the Company:")
api_scraper(u)
print (api_scraper(u))