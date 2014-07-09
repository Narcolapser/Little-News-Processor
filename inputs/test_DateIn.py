import unittest
import time
import datetime
from DateIn import Date


class TestReport (unittest.TestCase):

	def setUp(self):
		self.date = Date()
		self.dateTup = Date()
		
	def test_date(self):
		d = datetime.date.today()
		dtup = (d.year,d.month,d.day)
		dstr = '{0[0]},{0[1]:0>2},{0[2]:0>2}'.format(dtup)
		self.assertEqual(dstr,self.date.fetch())
	
	def test_date_tup(self):
		d = datetime.date.today()
		dtup = (d.year,d.month,d.day)
		self.assertEqual(self.date.getDateTuple(),dtup)


if __name__ == "__main__":
	unittest.main()
