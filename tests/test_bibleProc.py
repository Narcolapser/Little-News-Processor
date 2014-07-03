import unittest
import time
import datetime
from inputs.petra import Report


class TestReport (unittest.TestCase):

	def setUp(self):
		self.report = Report('tests/petra_sample.txt')
	
	def test_cost_centre(self):
		self.assertEqual(self.report.cost_centre,'2345JOHS')
