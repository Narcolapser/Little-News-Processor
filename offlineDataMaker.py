import inputs.bibleIn
import inputs.tldrnewsIn
import inputs.weatherIn

import pickle

kindle = ""

def run():
	data = []
	bib = inputs.bibleIn.BibleInput("inputs/bibleSchedule.csv")
	tldr = inputs.tldrnewsIn.TLDRNewsInput()
	wet = inputs.weatherIn.WUnderGroundInput()
	print("fectching bible")
	data.append(bib.fetch())
	print("done. Fetching news")
	data.append(tldr.fetch())
	print("done. Fetching weather")
	data.append(wet.fetch())
	print("done. outputing")
	f = open("fetches","w")
	f.write("data = " + str(data))
#	for i in data:
#		f.write(str(i)+"\n\n\n")
	print("Network complete")

if __name__ == "__main__":
	run()
