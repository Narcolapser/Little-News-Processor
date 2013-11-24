def put(data,location):
	f = open(location,"w")
	for i in data:
		f.write(i+"\n\n--------------====================--------------\n\n")
	f.close()
