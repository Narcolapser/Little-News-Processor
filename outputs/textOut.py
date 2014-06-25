class:
	def __init__(self,chapterSeperator=None):
		if chapterSeperator:
			self.CS = chapterSeperator
		else:
			self.CS = "\n\n--------------====================--------------\n\n"

	def put(self,data,location):
		f = open(location,"w")
		for i in data:
			f.write(i+self.CS)
		f.close()
