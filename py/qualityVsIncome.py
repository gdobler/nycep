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
		score = float(row[1])
		if score == -1:
			continue
		else:
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
			pa[park]
			pq[park]
		except:
			continue
		area = float(pa[park])
		areasum += area
		quality = float(pq[park])
		#print area, quality
		num += (area*quality)
	quality = num/(areasum+1*(areasum==0))
	avgQual[row] = quality

with open("../output/parkQualityByZip.csv", 'wb') as w:
	wr = csv.writer(w, delimiter = ",")
	for zipcode in avgQual:
		wr.writerow([zipcode, avgQual[zipcode]])



