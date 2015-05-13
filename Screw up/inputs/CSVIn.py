class CSVIn (object):
	'''
	This is a simple CSV input class designed to provide basic table manipulation. It is organized
	like a database, first you go down the rows, then you move cross the columns.
	'''
	def __init__(self,location,cell_delimiter=',',row_delimiter='\n'):
		'''
		Give a location for a CSV, and this will house it in a handy dandy format. 
		Optional: cell_delimiter (Default: ",")
		Optional: row_delimiter (Default: "\n"
		'''
		with open(location) as sch:
			self.file = sch.read()
		self.data = []
		for row in self.file.split(row_delimiter):
			drow = []
			for cell in row.split(cell_delimiter):
				drow.append(cell)
			data.append(drow)
	
	def fetch():
		'''
		retrieves the CSV in 2D list format.
		'''
		return self.data

class CSVSchedule (CSVIn):
	'''
	This is an extention of the simple CSV class above. It provides a more simple access to data
	that has been formated specificlly in the way of (year,month,day) addresses for lists or items
	of information.
	'''
	
	def getDate(self,year,month,day):
		'''
		Returns the list of items scheduled for the date given.
		'''
		years = []
		for row in self.data:
			if row[0] == str(year):
				years.append(row[1:])
		
		months = []
		for row in years:
			if row[0] == str(month):
				months.append(row[1:])
		
		days = []
		for row in months:
			if row[0] == str(day):
				days.append(row[1:])
		
		return days
	
	def getDateFromString(self,dateString):
		'''
		returns the list of items scheduled for the date given in the format of yyyy,mm,dd
		'''
		
		items = []
		for i in self.data:
			if dateString == '{0:0>4},{1:0>2},{2:0>2}'.format(i[0],i[1],i[2])
				items.append(i[3:])
		
		return items
