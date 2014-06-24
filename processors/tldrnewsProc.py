import tldrnewsIn

class:
	def __init__(self):
		pass

	def consume(data):
		ret = ""
		for i in data:
			ret += i[0]+"\n"
			ret += "\t"+i[1]+"\n\n"
		return ret+"\n"

if __name__ == "__main__":
	data = tldrnewsIn.fetch()
	print(consume(data))
