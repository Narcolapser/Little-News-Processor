import unittest
import time
import datetime
from petra import Report

class TestReport (unittest.TestCase):

	def setUp(self):
		self.report = Report('/home/toben/Downloads/r0055639.txt')
	
	def test_cost_centre(self):
		self.assertEqual(self.report.cost_centre,'3832ARCT')
	
	def test_period_start(self):
		self.assertEqual(self.report.period_start,datetime.date(2014,3,1))

	def test_period_finish(self):
		self.assertEqual(self.report.period_finish,datetime.date(2014,3,31))
		
	def test_currency(self):
		self.assertEqual(self.report.currency,'GBP')
	
	def test_requester(self):
		self.assertEqual(self.report.report_requester,'JULIAP')
	
	def test_gen_date(self):
		self.assertEqual(self.report.report_generated_date,datetime.date(2014,4,22))
		
	def test_total_debit(self):
		self.assertEqual(self.report.total_debit, 814.53)
	
	def test_total_credit(self):
		self.assertEqual(self.report.total_credit, 525.06)
	
	def test_net_balance(self): 
		self.assertEqual(self.report.net_balance, 289.47)
	
	def test_starting_balance(self): 
		self.assertEqual(self.report.starting_balance, 4619.63)
	
	def test_ending_balance(self): 
		self.assertEqual(self.report.ending_balance, 4330.16)
	
	def test_centre_count(self):
		self.assertEqual(len(self.report.centres),17)

class TestCentre(unittest.TestCase):
	def setUp(self):
		self.report = Report('/home/toben/Downloads/r0055639.txt')
	
	def test_centre_ID(self):
		self.report

if __name__ == '__main__':
	unittest.main()
