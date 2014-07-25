import csv
import matplotlib.pyplot as plt

def printdict(dictionary):
	for entry in dictionary:
		print entry, dictionary[entry]

zips = {}

with open("../data/ParkInZip.csv") as f:
	lines = csv.reader(f, delimiter = ",")
	lines.next()
	for line in lines:
		zipCode = line[0]
		zipArea = line[1]
		parkArea = line[3]
		if not zipCode in zips:
			zips[zipCode] = [zipArea]
			zips[zipCode].append(parkArea)
		else:
			zips[zipCode].append(parkArea)

# zips2 contains the pct of zip code covered by park land
zips2 = {}

for entry in zips:
	area = float(zips[entry][0])
	parkArea = 0
	for i in range(1, len(zips[entry])):
		parkArea += float(zips[entry][i])
	pctPark = parkArea/area*100
	zips2[entry] = [pctPark]


# define "small business" as < 250 employees

zbpZips = {}

with open("../output/zbp/zbp12detailCleaned.txt") as f:
	lines = csv.reader(f, delimiter = ",")
	lines.next()
	for line in lines:
		zipCode = line[0].strip("\"")

		if not zipCode in zbpZips:
			zbpZips[zipCode] = [float(line[3])]
			for i in range(4, 8):
				zbpZips[zipCode][0] += float(line[i])
			zbpZips[zipCode].append(float(line[9]))
			for i in range(10, 11):
				zbpZips[zipCode][1] += float(line[i])
		else:
			for i in range(3, 8):
				zbpZips[zipCode][0] += float(line[i])
			for i in range(9, 11):
				zbpZips[zipCode][1] += float(line[i])	


ratio = {}

for entry in zbpZips:
	smallBus = zbpZips[entry][0]
	bigBus = zbpZips[entry][1]
	if bigBus == 0:
		continue
	rat = smallBus/bigBus
	ratio[entry] = [rat]

# grab matching zip codes from both dictionaries

parkPcts = {}
busRatio = {}

for key in ratio:
	if key in zips2:
		parkPcts[key] = zips2[key]
		busRatio[key] = ratio[key]

xvals = []
yvals = []

for key in sorted(parkPcts):
	xvals.append(parkPcts[key])

for key in sorted(busRatio):
	yvals.append(busRatio[key])

plt.scatter(np.log10(xvals), yvals, color='black')
plt.xlim([-3,3])
plt.xlabel('Log of pct of ZIP code covered by parks')
plt.ylabel('Ratio of Small to Big Businesses (<250 workers)')
plt.title('Parks and Small Businesses')

from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('pctVsSmallBusRatio.pdf')
plt.savefig(pp, format='pdf')
pp.close()


# Annual Payroll

payroll = {}

with open("../output/zbp/zbp12totalsCleaned.txt") as f:
	lines = csv.reader(f, delimiter = ",")
	lines.next()
	for line in lines:
		zipCode = line[0].strip("\"")
		ap = float(line[8])
		payroll[zipCode] = ap

parkPcts2 = {}
annPayroll = {}

for key in payroll:
	if key in zips2:
		parkPcts2[key] = zips2[key]
		annPayroll[key] = payroll[key]

plot2x = []
plot2y = []

for key in sorted(parkPcts2):
	plot2x.append(parkPcts2[key])

for key in sorted(annPayroll):
	plot2y.append(annPayroll[key])

plt.scatter(np.log10(plot2x), np.log10(plot2y), color='black')
plt.xlabel('Log of pct of ZIP code covered by parks')
plt.ylabel('Log of Annual Payroll ($1000)')
plt.title('Parks and Annual Payroll')

pp = PdfPages('pctVsAnnualPayroll.pdf')
plt.savefig(pp, format='pdf')
pp.close()


# Total employees
employees = {}

with open("../output/zbp/zbp12totalsCleaned.txt") as f:
	lines = csv.reader(f, delimiter = ",")
	lines.next()
	for line in lines:
		zipCode = line[0].strip("\"")
		emp = float(line[4])
		employees[zipCode] = emp

marchEmployees = {}

for key in employees:
	if key in zips2:
		marchEmployees[key] = employees[key]

plot3x = []
plot3y = []

for key in sorted(parkPcts2):
	plot3x.append(parkPcts2[key])

for key in sorted(marchEmployees):
	plot3y.append(marchEmployees[key])

plt.scatter(np.log10(plot3x), plot3y, color='black')
plt.xlabel('Log of pct of ZIP code covered by parks')
plt.ylabel('Total Mid-March Employees')
plt.title('Parks and Total Employees')

pp = PdfPages('pctVsTotalEmployees.pdf')
plt.savefig(pp, format='pdf')
pp.close()


# Total Number of Establishments

establishments = {}

with open("../output/zbp/zbp12totalsCleaned.txt") as f:
	lines = csv.reader(f, delimiter = ",")
	lines.next()
	for line in lines:
		zipCode = line[0].strip("\"")
		est = float(line[9])
		establishments[zipCode] = est

totalEst = {}

for key in establishments:
	if key in zips2:
		totalEst[key] = establishments[key]

plot4x = []
plot4y = []

for key in sorted(parkPcts2):
	plot4x.append(parkPcts2[key])

for key in sorted(totalEst):
	plot4y.append(totalEst[key])

plt.scatter(np.log10(plot4x), plot4y, color='black')
plt.xlabel('Log of pct of ZIP code covered by parks')
plt.ylabel('Total Number of Establishments')
plt.title('Parks and Total Establishments')

pp = PdfPages('pctVsTotalEstablishments.pdf')
plt.savefig(pp, format='pdf')
pp.close()