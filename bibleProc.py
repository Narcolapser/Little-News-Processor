import bibleIn

def consume(verses):
	ret = ""
	for i in verses:
		out = ""
		for v in i:
			add = str(v[3])
			if (v[0] == 'Proverbs'):
				add = add.replace("\n\n","\n")
				add += "\n"
			out += add
		ret += out+"\n\n\n"
	return ret[:-3]

if __name__ == "__main__":
	verses = bibleIn.fetch()
	print(consume(verses))
