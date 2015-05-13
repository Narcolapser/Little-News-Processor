class TLDRNewsProc:
	def __init__(self):
		pass

	def consume(data):
		ret = ""
		for i in data:
			ret += i[0]+"\n"
			ret += "\t"+i[1]+"\n\n"
		return ret+"\n"
