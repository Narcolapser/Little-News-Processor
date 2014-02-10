import bibleIn
import tldrnewsIn
import weatherIn

import bibleProc
import tldrnewsProc
import weatherProc

import textOut
import htmlOut
import pdfOut

kindle = ""

def run():
	data = []
	print("fectching bible")
	data.append(bibleProc.consume(bibleIn.fetch()))
	print("done. Fetching news")
	data.append(tldrnewsProc.consume(tldrnewsIn.fetch()))
	print("done. Fetching weather")
	data.append(weatherProc.consume(weatherIn.fetch()))
	print("done. outputing")
	textOut.put(data,kindle+"dailyNews.txt")
	htmlOut.put(data,kindle+"dailyNews.html")
	pdfOut.put(data,kindle+"dailyNews")
	print("Network complete")

if __name__ == "__main__":
	run()
