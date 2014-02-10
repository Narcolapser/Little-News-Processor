import bibleIn
import tldrnewsIn
import weatherIn

import bibleProc
import tldrnewsProc
import weatherProc

import textOut
import htmlOut
import pdfOut

import pickle

kindle = ""

def run():
	data = []
	print("fectching bible")
	data.append(bibleIn.fetch())
	print("done. Fetching news")
	data.append(tldrnewsIn.fetch())
	print("done. Fetching weather")
	data.append(weatherIn.fetch())
	print("done. outputing")
	f = open("fetches","w")
	f.write("data = " + str(data))
#	for i in data:
#		f.write(str(i)+"\n\n\n")
	print("Network complete")

if __name__ == "__main__":
	run()
