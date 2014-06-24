class:
	def __init__(self):
		pass

	def put(self,data,location):
		f = open(location,"w")
		for i in data:
			f.write(i+"\n\n--------------====================--------------\n\n")
		f.close()
