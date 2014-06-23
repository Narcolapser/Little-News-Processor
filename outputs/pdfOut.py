import os

def put(data,location):
	os.system("wkhtmltopdf "+location+".html "+location+".pdf")
