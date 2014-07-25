import csv

zbp = []
data = {}

with open("../data/zbp/zbp12totals.txt", "rU") as f:
	zbp = f.readlines()

with open("../data/medianHHincomeZCTA.csv") as f:
	lines = csv.reader(f, delimiter = ",")
	lines.next()
	lines.next()
	for line in lines:
		zipcode = line[1]
		hhinc = line[3]
		if hhinc == '':
			hhinc = 0
		data[zipcode] = [hhinc]

#i = 0
#for row in zbp:
#	if (i == 0):
#		i += 1
#		continue
#	fields = row.split("\",\"")
#	zipcode = fields[0].strip('"')
#	totalEmployees = fields[4].strip('"')
#	annualPayroll = fields[8].strip('"')
#	totalEstablishments = fields[9].strip('"')
	#avgSalary = float(annualPayroll)/float(totalEmployees)
#	if zipcode in data:
#		data[zipcode].append([totalEmployees, annualPayroll, totalEstablishments])


def addYear(fileName, dictionary, ind):
	with open(fileName, "rU") as f:
		rows = csv.reader(f, delimiter = ",")
		rows.next()
		for row in rows:
			zc = row[0]
			if not zc in dictionary:
				dictionary[zc] = [float(row[ind])]
			else:
				dictionary[zc].append(float(row[ind]))

addYear('../output/zbp/12totals.txt', data, 4) # total employees
addYear('../output/zbp/12totals.txt', data, 8) # annual payroll
addYear('../output/zbp/12totals.txt', data, 9) # total establishments


with open("../output/parkQualityByZip.csv", "rU") as f:
	lines = csv.reader(f, delimiter = ",")
	for line in lines:
		zipcode = line[0]
		parkquality = line[1]
		try:
			data[zipcode].append(parkquality)
		except:
			continue

for entry in data:
	if len(data[entry]) == 4:
		data[entry].append(-1)

w = open('../data/featuresForMap.csv', 'wb')
wr = csv.writer(w, delimiter = ',')
wr.writerow(['zipcode', 'medianhhincome', 'employees', 'payroll', 'establishments', 'avgParkQuality'])
for entry in data:
	fields = [entry, data[entry][0], data[entry][1], data[entry][2], data[entry][3], data[entry][4]]
	wr.writerow(fields)


# plot quality v income:
import matplotlib.pyplot as plt

for entry in data:
	plt.scatter(data[entry][0], data[entry][4], color = 'k')

plt.ylim([-.25,1.25])
plt.xlabel("Median HH Income")
plt.ylabel("Area-Weighted Average Park Quality")
plt.title("Income and Park Quality")


from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('qualityvsincome.pdf')
plt.savefig(pp, format='pdf')
pp.close()
