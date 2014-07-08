import time

class Date (object):

	def __init__(self):
		pass

	def getTodayWellFormated(self):
		'''
		this function returns a well formated representation of today's date to make working
		with the csv connection easy.
		'''
		ltime = time.localtime()
		today = str(ltime.tm_year)+','
		if ltime.tm_mon<10:
			today += '0'+ str(ltime.tm_mon)+','
		else:
			today += str(ltime.tm_mon)+','

		if ltime.tm_mday < 10:
			today += '0' + str(ltime.tm_mday)
		else:
			today += str(ltime.tm_mday)
		return today
