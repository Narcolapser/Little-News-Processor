## This module is responsible for pulling in information related to my current support levels

import requests
import json
import csv

def clean_results(val):
	reader = csv.reader(val.split('\r\n')[:-1])
	headers = reader.__next__()
	ret = []
	
	for row in reader:
		record = {}
		for i,header in enumerate(headers):
			record[header] = row[i]
		ret.append(record)
	
	return ret

def fetch():
	auth = json.loads(open('caleb.passwd','r').read())
	auth = (auth['username'],auth['password'])

	url = 'https://secure.om.org/caleb/support/csvsupport.jsp'
	params = {'report':'all_don','period':'all_available','currency':'USD','startDate':'01-Jan-2013','endDate':'01-Jan-2020'}
	
	support = requests.get(url,params=params,auth=auth)
	
	support_text = support.content.decode()
	
	supportCSV = clean_results(support_text)
	
	return supportCSV


if __name__ == '__main__':
	print(fetch())
