import time

class Date (object):

	def __init__(self):
		pass

	def fetch(self):
		'''
		this function returns a well formated string representation of today's date to make working
		with the csv connection easy.
		'''
		ldate = self.getDateTuple()
		today = '{0[0]},{0[1]:0>2},{0[2]:0>2}'.format(ldate)
		return today
	
	def getDateTuple(self):
		ltime = time.localtime()
		year = ltime.tm_year
		month = ltime.tm_mon
		day = ltime.tm_mday
		return (year,month,day)
