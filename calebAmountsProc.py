import calebIn
import time

def consume(records):
	time_string = '%d-%b-%Y'
	months = ['January','February','March','April','May','June','July','August','September','October','November','December']

	sums = {}
	for r in records:
		rDate = time.strptime(r['Date'],time_string)
		if rDate.tm_year == 2015:
			if rDate.tm_mon in sums.keys():
				sums[rDate.tm_mon] += float(r['Gross (USD)'])
			else:
				sums[rDate.tm_mon] = float(r['Gross (USD)'])
	
	ret = "Caleb support monthly Totals:\n"
	for key in sums.keys():
		ret += '{0:.<40}{1}\n'.format(months[key-1],str(sums[key]))
	return ret


if __name__ == "__main__":
	print(consume(calebIn.fetch()))
