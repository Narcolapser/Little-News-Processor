from inputs.bibleIn import BibleInput
from inputs.tldrnewsIn import TLDRNewsInput
from inputs.weatherIn import WUnderGroundInput as WeatherIn

from processors.bibleProc import BibleProc
from processors.tldrnewsProc import TLDRNewsProc
from processors.weatherProc import WeatherProc

from outputs import textOut
from outputs import htmlOut
from outputs import pdfOut

kindle = ""

def run():
	data = []
	print("fectching bible")
	data.append(BibleProc().consume(BibleInput().fetch()))
	print("done. Fetching news")
	data.append(TLDRNewsProc().consume(TLDRNewsInput().fetch()))
	print("done. Fetching weather")
	data.append(WeatherProc().consume(WeatherIn().fetch()))
	print("done. outputing")
	textOut.put(data,kindle+"dailyNews.txt")
	htmlOut.put(data,kindle+"dailyNews.html")
	pdfOut.put(data,kindle+"dailyNews")
	print("Network complete")

if __name__ == "__main__":
	run()
