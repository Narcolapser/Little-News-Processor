import os

class PDFout:
	def __init__(self):
		pass

	def put(self,data,location):
		os.system("wkhtmltopdf "+location+".html "+location+".pdf")
