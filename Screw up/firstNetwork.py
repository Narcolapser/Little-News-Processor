from inputs import bibleIn
from inputs import tldrnewsIn

from processors import bibleProc
from processors import tldrnewsProc

from outputs import textOut

#kindle = "/media/toben/Kindle/documents/"
def run():
	data = []
	print("fectching bible")
	data.append(bibleProc.consume(bibleIn.fetch()))
	print("done. Fetching news")
	data.append(tldrnewsProc.consume(tldrnewsIn.fetch()))
	print("done. outputing")
	textOut.put(data,"/home/toben/Code/Little-News-Processor/sample.txt")
	print("Network complete")

if __name__ == "__main__":
	run()
