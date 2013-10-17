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

def translateTagLetters(val):
	
	while(val.find("&#")!=-1):
		loc = val.find("&#")
		cv = val[loc+2:loc+5]
		ret = val[:loc] + c + val[loc+5]