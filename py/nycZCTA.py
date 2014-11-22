import csv

zcta = []

with open("../data/zbp/ACS_12_5YR_B01003_with_ann.csv") as f:
	lines = csv.reader(f, delimiter = ",")
	lines.next()
	lines.next()
	for line in lines:
		zc = line[1]
		zcta.append(zc)

with open("../output/zbp/zcta.txt", "wb") as w:
	for row in zcta:
		w.write(row + '\n')