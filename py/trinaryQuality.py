import csv

tri = []

with open('../data/Parks/ParksCSV.csv','rU') as f:
	rows = csv.reader(f, delimiter = ",")
	rows.next()
	for row in rows:
		parkid = row[0]
		n1 = float(row[3])
		n2 = float(row[4])
		score = (n1 + n2)/2
		tri.append([parkid, score])

with open('../output/trinaryScore.csv', 'wb') as w:
	wr = csv.writer(w, delimiter = ",")
	for row in tri:
		wr.writerow(row)