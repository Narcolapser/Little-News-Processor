import bibleIn

def consume(verses):
	template = open("HTML Templates/bible.tp","r").read()
	ret = ""
	for i in verses:
		out = template
		out = out.replace("%chapter%",i[0][0])
		add = ""
		for v in i:
			add += v[3]
			add = add.replace("\n","<br/>")
		if (v[0] == 'Proverbs'):
			add = add.replace("<br/><br/>","<br/>")
			add += "<br/>"
		out = out.replace("%text%",add)
		ret += out+"<br/>"
	return ret[:-3]

if __name__ == "__main__":
	verses = bibleIn.fetch()
#	consume(verses)
	print(consume(verses))
