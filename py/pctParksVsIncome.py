import csv
import matplotlib.pyplot as plt
import numpy as np

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

# pct contains the pct of zip code covered by park land
pct = {}

for entry in zips:
	area = float(zips[entry][0])
	parkArea = 0
	for i in range(1, len(zips[entry])):
		parkArea += float(zips[entry][i])
	pctPark = parkArea/area*100
	pct[entry] = [pctPark]


# read in median hh income data
inc = {}

with open("../data/medianHHincomeZCTA.csv") as f:
	lines = csv.reader(f, delimiter = ",")
	lines.next()
	lines.next()
	for line in lines:
		zipcode = line[1]
		hhinc = line[3]
		if hhinc == '':
			hhinc = 0
		inc[zipcode] = [hhinc]

xvals = []
yvals = []
for entry in pct:
	pp = pct[entry]
	try:
		ic = inc[entry]
	except:
		continue
	#plot(np.log10(pp), ic)
	#data.append([pp, ic])
	xvals.append(pp)
	yvals.append(ic)


plt.scatter(np.log10(xvals), yvals, color='k')
plt.xlabel('Log of pct of ZIP code covered by Parks')
plt.ylabel('Median HH Income')
plt.title('Parks and Median Household Income')

from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('pctVsHHIncome.pdf')
plt.savefig(pp, format='pdf')
pp.close()
