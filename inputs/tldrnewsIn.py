import urllib.request

class TLDRNewsInput(object):

	def __init__(self,tags):
		if tags:
			self.tags = tags
		else:
			self.tags = ["world-news","science","tech","gaming"]


	def findall(foo,bar,offset=0):
		a = 0
		ret = []
		for i in range(foo.count(bar)):
			a = (foo.find(bar,a))
			ret.append(a+offset)
			a+=1
		return ret

	def getArticleStrings(val):
		openings = self.findall(val,"<article>")
		closings = self.findall(val,"</article>",10)
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
		val = self.replaceAll(val,"&#039;","'")
		val = self.replaceAll(val,"\\xe2\\x80\\x9c",'"')
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
		feed = self.pulldownFeed(tag)
		articles = self.getArticleStrings(feed)
		articles.pop(0)
		ret = []
		for article in articles:
			ret.append([self.translateTagLetters(tag+" : "+self.getArticleHeader(article)),self.getArticleBody(article)])
		return ret

	def fetch():
		ret = []
		for t in self.tags:
			ret+=self.fetchTag(t)
		return ret
