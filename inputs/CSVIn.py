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
#	def __init__(self,location,cell_delimiter=',',row_delimiter='\n'):
#		super().__init__()
#		self.years = {}
#		for row in self.data:
#			if row[0] not in self.years.keys():
#				self.years[row[0]] = {}
#		
#		for row in self.data:
#			if row[1] not in self.years[row[0]].keys():
#				self.years[row[0]][row[1]] = {}
#		
#		for row in self.data:
#			if row[2] not in self.years[row[0]][row[1]].keys():
#				if len(row[3:]) == 0:
#					self.years[row[0]][row[1]][row[2]] = []
#				elif len(row[3:]) == 1:
#					self.years[row[0]][row[1]][row[2]] = [row[3]]
#				else:
#					self.years[row[0]][row[1]][row[2]] = [row[3:]]
#			else:
#					self.years[row[0]][row[1]][row[2]].append([])
#				elif len(row[3:]) == 1:
#					self.years[row[0]][row[1]][row[2]].append([row[3]])
#				else:
#					self.years[row[0]][row[1]][row[2]].append([row[3:]])
		
#		for row in self.data:
#			if row[0] in self.dateData.keys():
#				if row[1] in self.dateData[row[0]].keys():
#					if row[2] in self.dateData[row[0]][row[1]].keys():
#						if len(row[3:]) == 1:
#							self.dateData[row[0]][row[1]][row[2]].append(row[3])
#						else:
#							self.dateData[row[0]][row[1]][row[2]].append(row[3:])
					
	
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
