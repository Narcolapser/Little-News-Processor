import datetime


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
	
	def __init__(self,path_to_report):
		with open(path_to_report) as petra_report:
			pr = petra_report.read()
		self.cost_centre = find_cost_centre(pr)
		self.period_start = find_period_start(pr)
		self.period_finish = find_period_finish(pr)
		self.currency = find_currency(pr)
		self.report_requester = find_requester(pr)
		self.report_generated_date = find_report_gen_date(pr)
		self.total_credit = find_total_credit(pr)
		self.total_debit = find_total_debit(pr)
		self.net_balance = find_net_balance(pr)
		self.starting_balance = find_starting_balance(pr)
		self.ending_balance = find_ending_balance(pr)
		centre_st = pr.find('3832ARCT',pr.find('End Balance   '))
		centres_s = pr[centre_st:].split('3832ARCT-')
		centres_s.pop(0)
		#print(len(centres_s),centre_st)
		self.centres = []
		for centre in centres_s:
			self.centres.append(Centre(centre))

class Centre(object):
	'''this class wraps the sub cost centres of the petra reports so that you can see the charges
	in your petra report by category'''
	ID = None
	category = None
	items = None
	centre_total_debit = None
	centre_total_credit = None
	
	def __init__(self,centre):
		#print(centre[:4])
		self.ID = int(centre[:4].replace(' ',''))
		cat_st = 5
		while centre[cat_st] == ' ':
			cat_st += 1
		self.category = centre[cat_st:centre.find(', ',cat_st)]
		lines = centre.split('\n')
		self.items = []
		sub_line = None
		for line in lines[1:]:
			if 'Sub Total:' in line:
				sub_line = line
				break
			self.items.append(Item(line))
		sub_st = sub_line.find('Sub Total:') + len('Sub Total: ')
		while sub_line[sub_st] == ' ':
			sub_st += 1
		sub_s = sub_line[sub_st:sub_line.find(' ',sub_st)].replace(',','')
		self.centre_total_debit = float(sub_s)
		
		sub_st += len(sub_s) + 1
		while sub_line[sub_st] == ' ':
			sub_st += 1
		sub_s = sub_line[sub_st:sub_line.find(' ',sub_st)].replace(',','')
		self.centre_total_credit = float(sub_s)

	def __str__(self):
		return 'ID: {0}\t Category: {1}\t tDebit: {2}\t tCredit: {3}\n'.format(self.ID,self.category,self.centre_total_debit,self.centre_total_credit)


class Item (object):

	def __init__(self, line):
		day = int(line[2:4])
		mon = months[line[5:8]]
		year = int(line[9:13])
		self.date = datetime.date(year,mon,day)
		code_st = 15
		self.code = line[code_st:line.find(' ',code_st)]
		v_st = line.find(' ',code_st)
		while v_st == ' ':
			v_st += 1
		value_s = line[v_st:line.find(' ',v_st)]
		self.value = value_s


'''
  31-Mar-2014  minrec3                      78.76                               Ministry Recharge - March - Archer 
  31-Mar-2014  minrec3                       5.25                               Europe AG - March  - Archer 
'''

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
	return float(pr[cred_st:cred_end])

def find_total_debit(pr):
	deb_st = pr.find('Grand Total') + len('Grand Total:')
	while pr[deb_st] == ' ':
		deb_st += 1
	deb_end = pr.find(' ',deb_st)
	return float(pr[deb_st:deb_end])

def find_net_balance(pr):
	net_st = pr.find('\nNet Balance:  ') + len('\nNet Balance:  ')
	while pr[net_st] == ' ':
		net_st += 1
	net_end = pr.find(' ',net_st)
	return float(pr[net_st:net_end])

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
	return float(pr[cred_st:cred_end].replace(',',''))

def find_ending_balance(pr):
	bal_end = pr.find(' CR ',pr.find(' CR ',pr.find('Grand Total:'))+4)
	bal_st = bal_end - 1
	while pr[bal_st] != ' ':
		bal_st -= 1
	bal_st += 1
	return float(pr[bal_st:bal_end].replace(',',''))
	
