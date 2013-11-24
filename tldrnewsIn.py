import urllib.request

def findall(foo,bar,offset=0):
	a = 0
	ret = []
	for i in range(foo.count(bar)):
		a = (foo.find(bar,a))
		ret.append(a+offset)
		a+=1
	return ret

def getArticleStrings(val):
	openings = findall(val,"<article>")
	closings = findall(val,"</article>",10)
	articles = []
	for i in range(len(openings)):
		articles.append(val[openings[i]:closings[i]])
	return articles

def getArticleBody(val):
	s = val.find("<p>")+3
	f = val.find("</p>",s)
	return val[s:f]

def getArticleHeader(val):
	s = val.find("<h1>")+4
	f = val.find("</h1>",s)
	return val[s:f]

#todo: Get this to translate more of the random junk out.
def translateTagLetters(val):
	val = replaceAll(val,"&#039;","'")
	val = replaceAll(val,"\\xe2\\x80\\x9c",'"')
	return val

def replaceAll(target,foo,bar):
	while(target.find(foo)!=-1):
		target = target.replace(foo,bar)
	return target


def pulldownFeed(tag):
	u = urllib.request.urlopen("http://toolong-didntread.com/tagged/"+tag)
	h = u.read()
	s = str(h)
	return s

def fetchTag(tag):
	feed = pulldownFeed(tag)
	articles = getArticleStrings(feed)
	articles.pop(0)
	ret = []
	for article in articles:
		ret.append([translateTagLetters(tag+" : "+getArticleHeader(article)),getArticleBody(article)])
	return ret
def fetch():
	tags = ["world-news","science","tech","gaming"]
	ret = []
	for t in tags:
		ret+=fetchTag(t)
	return ret
