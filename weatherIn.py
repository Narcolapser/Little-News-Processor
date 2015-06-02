key = """http://api.wunderground.com/api/b3d8129648ddfcc6/conditions/q/UK/Halesowen.json"""
forcast = """http://api.wunderground.com/api/b3d8129648ddfcc6/forecast/q/UK/Halesowen.json"""
import urllib.request
import json

def fetch():
	u = urllib.request.urlopen(forcast)
	return json.loads(u.read().decode("utf-8"))

if __name__ == "__main__":
	for i in fetch()['forecast']['simpleforecast']['forecastday']: print(i,'\n\n')
	#print(fetch())
