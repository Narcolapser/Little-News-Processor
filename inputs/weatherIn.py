key = """http://api.wunderground.com/api/b3d8129648ddfcc6/conditions/q/UK/Halesowen.json"""
forcast = """http://api.wunderground.com/api/b3d8129648ddfcc6/forecast/q/UK/Halesowen.json"""
import urllib.request
import json

class WUnderGroundInput (object):

	def __init__(self,key=None,country=None,city=None):
		'''key= you weather underground API key.
		country = the country code for the country you are searching in. e.g. UK
		city = the city you want the weather for. e.g. Halesowen.
		defaults are UK, Halesowen. Default while I'm still in pre-alpha is my key. but should 
		other people start using this. My key will disappear.
		'''
		if key:	self.key = key
		else:	self.key = 'b3d8129648ddfcc6'
		self.forcast = 'http://api.wunderground.com/api/{0}/forecast/q/{1}/{2}.json'
		
		if country: self.country = country
		else:		self.country = 'UK'
		
		if city:	self.city = city
		else:		self.city = 'Halesowen'

	def fetch(self):
		'''get the forecast for the location instantiated here.'''
		u = urllib.request.urlopen(forcast)
		return json.loads(u.read().decode("utf-8"))

if __name__ == "__main__":
	wet = WUnderGroundInput()
	print(wet.fetch())
