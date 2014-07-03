#this script pulls in the date from a csv file, cross refernces it with the bible sqlite db and then
#out puts a section of text appropriate for the day. First I'm just going to get proverbs working.

import time
import sqlite3

class BibleInput(object):
	'''
	A class for pulling in bible information from a sqlite database and a csv that has been
	provided.
	'''
	
	schedule = None
	
	def __init__(self,schedule=None):
		if schedule is None:
			schedule = "bibleSchedule.csv"
		else:
			self.schedule = schedule
		print(self.schedule)

	def getTodayWellFormated(self):
		'''this function returns a well formated representation of today's date to make working
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

	def cleanRefs(self,val):
		'''val=bible verses to be cleaned. Takes a section of scripture and removes 'verse' and
		'chapter' and 'book' so that it reads nicely.
		'''
		refs = []
		for i in val:
			r = i.split(',')
			ref = {}
			if len(r) > 5:
				ref['verse'] = r[5]
			if len(r) > 4:
				ref['chapter'] = r[4]
			if len(r) > 3:
				ref['book'] = r[3]
			refs.append(ref)
		return refs

	def getTodaysReferences(self):
		'''takes today's date and the references made in the csv file to get what section of 
		scripture out to be returned for today.
		'''
		today = self.getTodayWellFormated()

		f = open(self.schedule,"r")
		ins = f.readlines()

		rawRefs = []
		for i in ins:
			if today in i: rawRefs.append(i.replace('\n',''))

		refs = self.cleanRefs(rawRefs)
		return refs

	def getVersesFromDB(self,ref):
		'''ref={book:'desired_book',chapter:#}->requested chapters if they exist.'''
		db = sqlite3.connect('/home/toben/Code/Little-News-Processor/bible.db')
		c = db.cursor()

		query = 'SELECT * FROM verse WHERE book LIKE {0} AND chapter={1}'.format(ref['book'],ref['chapter'])
		#query = 'SELECT * FROM verse WHERE book LIKE "Proverbs" AND chapter=6'

		c.execute(query)

		ref = c.fetchall()
		return ref

	def fetch(self):
		'''fetch method for the bible input pluggin.'''
		verses = []
		for r in self.getTodaysReferences():
			verses.append(self.getVersesFromDB(r))
		return verses
