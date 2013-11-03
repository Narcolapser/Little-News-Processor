key = """http://api.wunderground.com/api/b3d8129648ddfcc6/conditions/q/UK/Halesowen.json"""

import urllib.request

def getWeatherJson():
	u = urllib.request.openurl(key)
	return u.read()

print(getWeatherJson())
