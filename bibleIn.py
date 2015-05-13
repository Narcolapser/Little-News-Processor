#this script pulls in the date from a csv file, cross refernces it with the bible sqlite db and then
#out puts a section of text appropriate for the day. First I'm just going to get proverbs working.

import time
import sqlite3

def getTodayWellFormated():
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

def cleanRefs(val):
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

def getTodaysReferences():
	today = getTodayWellFormated()

	f = open("bibleSchedule.csv","r")
	ins = f.readlines()

	rawRefs = []
	for i in ins:
		if today in i: rawRefs.append(i.replace('\n',''))
	
	refs = cleanRefs(rawRefs)
	return refs

def getVersesFromDB(ref):
	db = sqlite3.connect('/home/toben/Code/Little-News-Processor/bible.db')
	c = db.cursor()
	
	query = 'SELECT * FROM verse WHERE book LIKE "'+ref['book']+'" AND chapter='+ref['chapter']#+" AND verse<5"
	#query = 'SELECT * FROM verse WHERE book LIKE "Proverbs" AND chapter=6'
	
	c.execute(query)
	
	ref = c.fetchall()
	return ref

def fetch():
	verses = []
	for r in getTodaysReferences():
		verses.append(getVersesFromDB(r))
	return verses

if __name__ == "__main__":
	print(fetch())
