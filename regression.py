'''
Program:	Little-News-Processor (LNP) Testing suite
Programmer:	Toben "Narcolapser" Archer
Version:	0.4

This script is the one responsible for tending to the testing of all of the pluggins available to 
LNP. It is stored at the root to make importing of the unit tests and the pluggins that they depend
on easy to load.

'''

import unittest
import os
import importlib

#def findTests():
#	tests = []
#	testsDir = os.listdir('./tests')
#	for i in testsDir:
#		if 'test' in i and '.py' in i:
#			tests.append(i)
#	return tests

#def importTests(testFiles):
#	testPKGs = []
#	for i in testFiles:
#		testPKGs.append(importlib.import_module('tests.{0}'.format(i[:-3])))
#	return testPKGs

#def buildSuite(testPKGs):
#	for mod in testPKGs:
#		unittest.defaultTestLoader.loadTestsFromModule(mod)



def run():
	'''
	the main call of the test master class. Call this and get the results of all the tests being run
	'''
#	testFiles = findTests()
#	testPKGs = importTests(testFiles)
#	print(testPKGs)
	
	tests = unittest.defaultTestLoader.discover('tests')
	res = unittest.TestResult()
	for t in tests:
		print(t.run(res))
	return res

if __name__ == "__main__":
	print(run())

