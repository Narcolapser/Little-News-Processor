#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
Petra Report python wrapper library.

The purpose of this library is to elevate petra reports into first class python objects. The 
library is made up of 3 classes: Report, Centre, and Item. Report is the parent class. It houses
all of the information unique to any given report. the centre, the currency, etc etc. Centre is
the individual sub cost centres in the report: telephone, gas, electric, etc. And lastly Item is
the actual values transfered around. So the organization looks something like:

Report:
	cost_centre = ''
	period_start = None
	period_finish = None
	currency = 'GBP'
	report_requester = ''
	report_generated_date = None
	total_credit = None
	total_debit = None
	net_balance = None
	starting_balance = None
	ending_balance = None
	centres = list:
		ID = None
		category = None
		centre_total_debit = None
		centre_total_credit = None
		items = list:
			date
			code
			value

so to access the value of a certain item you'd go:
report.centres[2].items[0].value

I also left all the functions for finding the various parts of the report as static methods that
only require you to pass a string of the petra report to it to get the value out. so you can also
call these methods individually if you just need one part and not the whole.

This can also be used as a script in a pipeline:
petra.py path_to_report | grep 'ending_balance'

or can translate petra reports into json files:
petra.py path_to_report path_to_output_json

'''

import datetime
import sys
import json
import time

class Report(object):
	'''this class has the purpose of elevating a petra report into a python object that is easily 
	used by other projects. It's one paramater is a path to a petra report'''
	cost_centre = ''
	period_start = None
	period_finish = None
	currency = 'GBP'
	report_requester = ''
	report_generated_date = None
	total_credit = None
	total_debit = None
	net_balance = None
	starting_balance = None
	ending_balance = None
	centres = None
	
	def update(self):
		report_requester = 'merged'
		report_generated_date = None
		
		td = 0.0
		tc = 0.0
		nb = 0.0

		for c in self.centres:
			td += c.centre_total_debit
			tc += c.centre_total_credit
			
		nb = tc + td
		
		self.total_credit = tc
		self.total_debit = td
		self.net_balance = nb
	
	def __init__(self,path_to_report=None,pr=None):
		if path_to_report:
			with open(path_to_report) as petra_report:
				pr = petra_report.read()

		self.cost_centre = find_cost_centre(pr)
		self.period_start = find_period_start(pr)
		self.period_finish = find_period_finish(pr)
		self.currency = find_currency(pr)
		self.report_requester = find_requester(pr)
		self.report_generated_date = find_report_gen_date(pr)

		gv = find_grand_values(pr)
		self.total_credit = gv[0]
		self.total_debit = gv[1]
		self.starting_balance = gv[2]
		self.ending_balance = gv[3]

		self.net_balance = find_net_balance(pr)
		centre_st = pr.find('3832ARCT',pr.find('End Balance   '))
		centres_s = pr[centre_st:].split('3832ARCT-')
		centres_s.pop(0)

		self.centres = []
		for centre in centres_s:
			self.centres.append(Centre(centre))


	def merge(self,val):
		for c in self.val:
			if c in self:
				self.get_centre(c.ID).merge(c)
			else:
				self.centres.append(c)
	
		period_start = None
		period_finish = None
	
		time_string = '%Y-%m-%d'
		s_start = time.strftime(self.period_start,time_string)
		v_start = time.strftime(val.period_start,time_string)
		
		s_finish = time.strftime(self.period_finish,time_string)
		v_finish = time.strftime(self.period_finish,time_string)
		
		

	def __contains__(self,centre):
		for c in self.centres:
			if c.ID == centre.ID: return True
		return False
	
	def get_centre(self,ID):
		for c in self.centres:
			if c.ID == ID:
				return c

class Centre(object):
	'''this class wraps the sub cost centres of the petra reports so that you can see the charges
	in your petra report by category'''
	ID = None
	category = None
	centre_total_debit = None
	centre_total_credit = None
	items = None
	
	def __init__(self,centre):
		#Cost Centre ID
		self.ID = int(centre[:4].replace(' ',''))
		
		#Cost Centre Category
		cat_st = 5
		while centre[cat_st] == ' ':
			cat_st += 1
		self.category = centre[cat_st:centre.find(', ',cat_st)]
		
		#cost centre Items
		lines = centre.split('\n')
		self.items = []
		sub_line = None
		for line in lines[1:]:
			if 'Sub Total:' in line:
				sub_line = line
				break
			self.items.append(Item(line))
		
		#cost centre total debit
		sub_st = sub_line.find('Sub Total:') + len('Sub Total: ')
		while sub_line[sub_st] == ' ':
			sub_st += 1
		sub_s = sub_line[sub_st:sub_line.find(' ',sub_st)].replace(',','')
		self.centre_total_debit = float(sub_s.replace(',',''))
		
		#cost centre total credit
		sub_st += len(sub_s) + 1
		while sub_line[sub_st] == ' ':
			sub_st += 1
		sub_s = sub_line[sub_st:sub_line.find(' ',sub_st)].replace(',','')
		self.centre_total_credit = float(sub_s.replace(',',''))

	def __str__(self):
		return 'ID: {0}\t Category: {1}\t tDebit: {2}\t tCredit: {3}\n'.format(self.ID,self.category,self.centre_total_debit,self.centre_total_credit)
	
	def merge(self,val):
		for record in val.items:
			if record not in self:
				self.items.append(record)
		
		self.update()
	
	def __contains(self,val):
		for i in self.items:
			if val.code == i.code:
				if val.value == i.value:
					if val.date == i.date:
						if val.purpose == i.purpose:
							return True
		return False
	
	def update(self):
		creds = 0.0
		debs = 0.0
		for i in self.items:
			if i.value >= 0:
				creds += i.value
			else:
				debs += i.value

		self.centre_total_credit = creds
		self.centre_total_debit = debs


class Item (object):
	
	date = None
	code = None
	value = None
	purpose = None

	def __init__(self, line):
		day = int(line[2:4])
		mon = months[line[5:8]]
		year = int(line[9:13])
		self.date = datetime.date(year,mon,day)
		code_st = 15
		self.code = line[code_st:line.find(' ',code_st)]
		v_st = 40
		while line[v_st] == ' ':
			v_st += 1
		v_end = line.find(' ',v_st)
		value_s = line[v_st:v_end]
		if v_end < 50:
			self.value = float(value_s.replace(',','')) * (-1)
		else:
			self.value = float(value_s.replace(',',''))
		
		purpose = line[81:]




def find_cost_centre(pr):
	cen_st = pr.find('Account Detail (') + len('Account Detail (')
	return pr[cen_st:cen_st+8]

months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

def find_period_start(pr):
	per_st = pr.find('Period: ') + len('Period: ')
	date_s = pr[per_st:per_st+len('01-Mar-2014')]
	date_list = date_s.split('-')
	mon = months[date_list[1]]
	return datetime.date(int(date_list[2]),mon,int(date_list[0]))

def find_period_finish(pr):
	per_st = pr.find('TO',pr.find('Period: ')) + len('TO ')
	date_s = pr[per_st:per_st+len('01-Mar-2014')]
	date_list = date_s.split('-')
	mon = months[date_list[1]]
	return datetime.date(int(date_list[2]),mon,int(date_list[0]))

def find_currency(pr):
	cur_st = pr.find('Currency: ') + len('Currency: ')
	return pr[cur_st:cur_st+3]

def find_requester(pr):
	req_st = pr.find('Report requested by: ') + len('Report requested by: ')
	req_end = pr.find('   ',req_st)
	return pr[req_st:req_end]

def find_report_gen_date(pr):
	per_st = pr.find('\n') - len(' 22-Apr-2014 ')
	date_s = pr[per_st:per_st+len(' 01-Mar-2014')]
	date_list = date_s.split('-')
	mon = months[date_list[1]]
	return datetime.date(int(date_list[2]),mon,int(date_list[0]))

def find_grand_values(pr):
	rows = pr.split('\n')
	gr = ''
	if 'Grand Total:' in rows[-2]:
		gr = rows[-2]
	elif 'Grand Total:' in rows[-3]:
		gr = rows[-3]
	else:
		for row in rows:
			if 'Grand Total:' in row:
				gr = row
				break
	
	td = find_total_debit(gr)
	tc = find_total_credit(gr)
	sb = find_starting_balance(gr)
	eb = find_ending_balance(gr)
	return (td,tc,sb,eb)

def find_total_debit(pr):
	deb_st = pr[14:50]
	deb_st = float(deb_st.replace(',',''))
	return deb_st

def find_total_credit(pr):
	cred_st = pr[51:71]
	cred_st = float(cred_st.replace(',',''))
	return cred_st

def find_starting_balance(pr):
	st_bal = pr[72:105]
	sign = pr[105:109]
	st_bal = float(st_bal.replace(',',''))
	if 'DR' in sign:
		st_bal *= (-1)
	return st_bal

def find_ending_balance(pr):
	end_bal = pr[109:128]
	sign = pr[128:]
	end_bal = float(end_bal.replace(',',''))
	if 'DR' in sign:
		end_bal *= (-1)
	return end_bal


def find_net_balance(pr):
	net_st = pr.split('\n')[-1]
	if 'Net Balance:' not in net_st:
		net_st = pr.split('\n')[-2]

	ret = float(net_st[14:].replace(',',''))
	if (len(net_st)) > 55:
		ret *= (-1)

	return ret

usage = '''Usage of petra.py: (are you using python3?)
Pass zero arguments to read this usage message:
petra.py

Pass one argument to output to screen or pipe:
petra.py path_to_report

Pass two arguments to output to a file:
petra.py path_to_report path_to_output_json

Pass three arguments to feel like an over-achiever:
petra.py path_to_report path_to_output_json brownie_points
'''

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print(usage)
		sys.exit()
	rep = Report(sys.argv[1])
	jout = {}
	jout['cost_centre'] = rep.cost_centre
	jout['period_start'] = str(rep.period_start)
	jout['period_finish'] = str(rep.period_finish)
	jout['currency'] = rep.currency
	jout['report_requester'] = rep.report_requester
	jout['report_generated_date'] = str(rep.report_generated_date)
	jout['total_credit'] = rep.total_credit
	jout['total_debit'] = rep.total_debit
	jout['net_balance'] = rep.net_balance
	jout['starting_balance'] = rep.starting_balance
	jout['ending_balance'] = rep.ending_balance
	jout['centres'] = []
	for centre in rep.centres:
		cout = {}
		cout['ID'] = centre.ID
		cout['category'] = centre.category
		cout['centre_total_debit'] = centre.centre_total_debit
		cout['centre_total_credit'] = centre.centre_total_credit
		cout['items'] = []
		for item in centre.items:
			iout = {}
			iout['date'] = str(item.date)
			iout['code'] = item.code
			iout['value'] = item.value
			cout['items'].append(iout)
		jout['centres'].append(cout)
	if len(sys.argv) == 3:
		with open(sys.argv[2],'w') as outFile:
			outFile.write(json.dumps(jout,sort_keys=True,indent=4,separators=(',',':')))
	else:
		print(json.dumps(jout,sort_keys=True,indent=4,separators=(',',':')))

'''
code grave yard:
def find_total_credit(pr):
	cred_st = pr.find('Grand Total') + len('Grand Total:')
	##get to where the debit value is.
	while pr[cred_st] == ' ':
		cred_st += 1
	##get past debit.
	while pr[cred_st] != ' ':
		cred_st += 1
	#and now find credit.
	while pr[cred_st] == ' ':
		cred_st += 1
	cred_end = pr.find(' ',cred_st)
	return float(pr[cred_st:cred_end].replace(',',''))

def find_total_debit(pr):
	deb_st = pr.find('Grand Total') + len('Grand Total:')
	while pr[deb_st] == ' ':
		deb_st += 1
	deb_end = pr.find(' ',deb_st)
	return float(pr[deb_st:deb_end].replace(',',''))

def find_net_balance(pr):
	net_st = pr.find('\nNet Balance:  ') + len('\nNet Balance:  ')
	while pr[net_st] == ' ':
		net_st += 1
	net_end = pr.find(' ',net_st)

	ret = pr[net_st:net_end].replace(',','')
	return float(ret)

def find_starting_balance(pr):
	cred_st = pr.find('Grand Total') + len('Grand Total:')
	##get to where the debit value is.
	while pr[cred_st] == ' ':
		cred_st += 1
	##get past debit.
	while pr[cred_st] != ' ':
		cred_st += 1
	#and now find credit.
	while pr[cred_st] == ' ':
		cred_st += 1
	#now get past credit
	while pr[cred_st] != ' ':
		cred_st += 1
	#lastly get to stating balance
	while pr[cred_st] == ' ':
		cred_st += 1
	cred_end = pr.find(' ',cred_st)
	
	ret = pr[cred_st:cred_end].replace(',','')
	return float(ret)

def find_ending_balance(pr):
	bal_end = pr.find(' CR ',pr.find(' CR ',pr.find('Grand Total:'))+4)
	bal_st = bal_end - 1
	while pr[bal_st] != ' ':
		bal_st -= 1
	bal_st += 1
	
	ret = pr[bal_st:bal_end].replace(',','')
	print(ret)
	return float(ret)
'''
