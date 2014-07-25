import csv

# dictionary to store park id and zip code it falls within
pz = {}
zipcodes = []

with open("../output/parkCentroidsByZip.csv", 'rU') as f:
	rows = csv.reader(f, delimiter = ",")
	rows.next()
	for row in rows:
		parkId = row[2]
		containingZip = row[12]
		if not containingZip in pz:
			pz[containingZip] = [parkId]
		else:
			pz[containingZip].append(parkId)

# dictionary to store park id and its score
pq = {}

with open("../output/trinaryScore.csv", 'rU') as f:
	rows = csv.reader(f, delimiter = ",")
	for row in rows:
		parkId = row[0]
		score = row[1]
		pq[parkId] = score

pa = {}

with open("../output/DPR_ParksProperties_001_nogeom.csv", "ru") as f:
	rows = csv.reader(f, delimiter = ",")
	rows.next()
	for row in rows:
		parkId = row[4]
		area = float(row[6])
		pa[parkId] = area

avgQual = {}

for row in pz:
	areasum = 0
	num = 0
	for park in pz[row]:
		#print row, park
		try:
			area = float(pa[park])
			areasum += area
			quality = float(pq[park])
			num += (quality*area)
		except:
			continue
	quality = num/areasum
	avgQual[row] = quality

with open("../output/parkQualityByZip.csv", 'wb') as w:
	wr = csv.writer(w, delimiter = ",")
	for zipcode in avgQual:
		wr.writerow([zipcode, avgQual[zipcode]])

