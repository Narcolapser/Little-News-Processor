import unittest
import time
import datetime
from inputs.petra import Report

class TestReport (unittest.TestCase):

	def setUp(self):
		self.report = Report('tests/petra_sample.txt')
	
	def test_cost_centre(self):
		self.assertEqual(self.report.cost_centre,'2345JOHS')
	
	def test_period_start(self):
		self.assertEqual(self.report.period_start,datetime.date(2014,1,1))

	def test_period_finish(self):
		self.assertEqual(self.report.period_finish,datetime.date(2014,2,28))
		
	def test_currency(self):
		self.assertEqual(self.report.currency,'GBP')
	
	def test_requester(self):
		self.assertEqual(self.report.report_requester,'CALLIC')
	
	def test_gen_date(self):
		self.assertEqual(self.report.report_generated_date,datetime.date(2014,4,10))
		
	def test_total_debit(self):
		self.assertEqual(self.report.total_debit, 1770.48)
	
	def test_total_credit(self):
		self.assertEqual(self.report.total_credit, 1256.04)
	
	def test_net_balance(self): 
		self.assertEqual(self.report.net_balance, 514.44)
	
	def test_starting_balance(self): 
		self.assertEqual(self.report.starting_balance, 5134.07)
	
	def test_ending_balance(self): 
		self.assertEqual(self.report.ending_balance, 4619.63)
	
	def test_centre_count(self):
		self.assertEqual(len(self.report.centres),16)

class TestCentre(unittest.TestCase):
	def setUp(self):
		self.report = Report('tests/petra_sample.txt')
		self.minrec = None
		for c in self.report.centres:
			if c.ID == 5004:
				self.minrec = c
				break
	
	def test_centre_ID(self):
		self.assertEqual(self.minrec.ID,5004)
	
	def test_category(self):
		self.assertEqual(self.minrec.category,'Internal Recharges')
	
	def test_items_count(self):
		self.assertEqual(len(self.minrec.items),2)
	
	def test_centre_total_debit(self):
		self.assertEqual(self.minrec.centre_total_credit,0.0)

	def test_centre_total_credit(self):
		self.assertEqual(self.minrec.centre_total_debit,84.01)

class TestItem(unittest.TestCase):
	def setUp(self):
		self.report = Report('tests/petra_sample.txt')
		self.minrec = None
		self.ich = None
		for c in self.report.centres:
			if c.ID == 5004:
				self.minrec = c
			if c.ID == 1100:
				self.ich = c

	def test_item_date(self):
		d = datetime.date(2014,3,31)
		self.assertEqual(d,self.minrec.items[0].date)
		self.assertEqual(d,self.minrec.items[1].date)
		self.assertEqual(d,self.ich.items[0].date)

	def test_item_code(self):
		self.assertEqual('minrec3',self.minrec.items[0].code)
		self.assertEqual('minrec3',self.minrec.items[1].code)
		self.assertEqual('ich3',self.ich.items[0].code)

	def test_item_value(self):
		self.assertEqual(-78.76,self.minrec.items[0].value)
		self.assertEqual(-5.25,self.minrec.items[1].value)
		self.assertEqual(525.06,self.ich.items[0].value)


if __name__ == '__main__':
	unittest.main()
