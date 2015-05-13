import bibleIn
import tldrnewsIn
import weatherIn
import calebIn

import bibleProc
import tldrnewsProc
import weatherProc
import calebAmountsProc
import calebSupportersProc

import textOut

kindle = "/media/toben/Kindle/documents/"
#kindle = '/home/toben/Code/Little-News-Processor/'

def run():
	caleb_data = calebIn.fetch()
	data = []

	print("fectching bible")
	data.append(bibleProc.consume(bibleIn.fetch()))

	print("done. Fetching weather")
	data.append(weatherProc.consume(weatherIn.fetch()))

	print("done. Fetching support stats")
	data.append(calebAmountsProc.consume(caleb_data))
	data.append(calebSupportersProc.consume(caleb_data))

	print("done. Fetching news")
	data.append(tldrnewsProc.consume(tldrnewsIn.fetch()))

	print("done. outputing")
	textOut.put(data,kindle+"dailyNews.txt")
	print("Network complete")

if __name__ == "__main__":
	run()
