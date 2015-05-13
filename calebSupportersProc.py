import calebIn
import time

def consume(records):
	time_string = '%d-%b-%Y'
	months = ['January','February','March','April','May','June','July','August','September','October','November','December']

	donations = {}
	for r in records:
		rDate = time.strptime(r['Date'],time_string)
		if rDate.tm_year == 2015:
			if rDate.tm_mon not in donations.keys():
				donations[rDate.tm_mon] = []
			donations[rDate.tm_mon].append((r['Donor Name'],float(r['Gross (USD)'])))
	
	ret = "{:^47}\n".format("Supporter Donations")
	keys = list(donations.keys())
	keys.sort(reverse=True)
	for key in keys:
		ret += "{:^47}\n".format(months[key-1])
		donations[key].sort()
		for donation in donations[key]:
			ytd = donation[1]
			for i in range(key)[1:]:
				for j in donations[i]:
					if donation[0] == j[0]:
						ytd += j[1]
			ret += "{0:.<35}${1:7.2f} ${2:7.2f}\n".format(donation[0],donation[1],ytd)
	return ret


if __name__ == "__main__":
	print(consume(calebIn.fetch()))
