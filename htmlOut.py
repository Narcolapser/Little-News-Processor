def put(data,location):
	f = open(location,"w")
	f.write("<HTML>\n")
	for i in data:
#		f.write("<p>"+i+"</p>\n")
		f.write(i)
	f.write("</HTML>")
	f.close()
