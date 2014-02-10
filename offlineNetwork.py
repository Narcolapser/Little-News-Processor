from offlineData import data as odata

print(len(odata))

import bibleProcHTML
import tldrnewsProc
import weatherProc

import textOut
import htmlOut
import pdfOut

kindle = ""

def run():
	data = []
	print("fectching bible")
	data.append(bibleProcHTML.consume(odata[0]))
#	print("done. Fetching news")
#	data.append(tldrnewsProc.consume(odata[1]))
#	print("done. Fetching weather")
#	data.append(weatherProc.consume(odata[2]))
#	print("done. outputing")
#	textOut.put(data,kindle+"dailyNews.txt")
	htmlOut.put(data,kindle+"dailyNews.html")
	pdfOut.put(data,kindle+"dailyNews")
	print("Network complete")

if __name__ == "__main__":
	run()
