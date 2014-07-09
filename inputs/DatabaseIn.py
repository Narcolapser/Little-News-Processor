import sqlite3

class DB (object):
	'''
	this is a simple database retriving input for LNP. This input will simply load the entire contents
	of a table. It mostly serves as a base class for which other classes might be derived. 
	'''
	def __init__(self,location,table):
		'''
		Takes a location of a database, and the table which you want returned.
		'''
		self.db = sqlite3.connect(location)
		self.table = table

	def fetch(self):
		'''
		retrieves the entire table specified in init.
		'''
		c = self.db.cursor()
		c.execute("SELECT * FROM {0}".format(self.table))
		return c.fetchall()
		
class BibleDB (DB):
	'''
	Derivied class from the DB class. this one specifically focuses on bible databases.
	'''
	def getVerse(self,book,chapter,verse):
		query = 'SELECT * FROM verse WHERE book LIKE {0} AND chapter={1} AND verse={2}'.format(book,chapter,verse)
		c = self.db.cursor()
		c.execute(query)
		return c.fetchall()
	
	def getChapter(self,book,chapter):
		query = 'SELECT * FROM verse WHERE book LIKE {0} AND chapter={1}'.format(book,chapter)
		c = self.db.cursor()
		c.execute(query)
		return c.fetchall()
