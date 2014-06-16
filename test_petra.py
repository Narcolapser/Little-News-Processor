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

#	def test_eq(self):
#		v5 = Vector(0,0)
#		v5.x = 5
#		v5.y = 5
#		self.assertEqual(v5,self.vec5)
#		self.assertTrue(v5 == self.vec5)
#		self.assertTrue((v5 == self.vec1) is False)
#	
#	def test_ne(self):
#		v5 = Vector(0,0)
#		v5.x = 5
#		v5.y = 5
#		self.assertEqual(v5,self.vec5)
#		self.assertTrue(v5 != self.vec1)
#		self.assertTrue((v5 != self.vec5) is False)
#	
#	def test_add(self):
#		v4 = self.vecu + self.veci
#		self.assertEqual(v4,Vector(4,4))
#		self.assertEqual(v4+self.vec1,self.vec5)
#	
#	def test_scale(self):
#		v5 = self.vec1*4
#		self.assertEqual(v5,self.vec5)
#		self.assertRaises(TypeError,v5.__mul__,self.vec5)
#	
#	def test_dot(self):
#		self.assertEqual(self.vecu.dot(self.veci),32)
#	
#	def test_str(self):
#		self.assertEqual(str("{'y': 5, 'x': 5}"),str(self.vec5))
#		#time.sleep(10)


if __name__ == '__main__':
	unittest.main()
