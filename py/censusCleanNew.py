import csv
import numpy as np

fileName = "../data/censusData/AvgHHSizeByAge/DEC_10_SF1_P17_with_ann.csv"

data = {}

def addFeatures(fileName, dictionary):
	with open(fileName) as f:
		lines = csv.reader(f, delimiter = ",")
		lines.next()
		lines.next()
		for line in lines:
			geoid = line[1]
			ct = float(geoid[5:11])*.01
			bn = float(geoid[11:])
			data = line[3:]
			length = len(line)

			if not geoid in dictionary:
				dictionary[geoid] = [float(line[3])]
				for i in range(4, length):
					if not "(r" in line[i]:
						dictionary[geoid].append(float(line[i]))
					else:
						loc = line[i].index('(')
						new = line[i][:loc]
						dictionary[geoid].append(float(new))
			else:
				for i in range(3, length):
					if not "(r" in line[i]:
						dictionary[geoid].append(float(line[i]))
					else:
						loc = line[i].index('(')
						new = line[i][:loc]
						dictionary[geoid].append(float(new))

addFeatures("../data/censusData/AvgHHSizeByAge/DEC_10_SF1_P17_with_ann.csv", data)
addFeatures("../data/censusData/OccupancyStatus/DEC_10_PL_H1_with_ann.csv", data)
addFeatures("../data/censusData/SexByAge/DEC_10_SF1_P12_with_ann.csv", data)
addFeatures("../data/censusData/Tenure/DEC_10_SF1_H4_with_ann.csv", data)

nBlocks = len(data)
nFeats = 0

for block in data:
	nFeats = len(data[block])
	break

#print nBlocks, nFeats

featVect = np.zeros(shape = (nBlocks, nFeats))

i = 0
j = 0
for block in data:
	for feature in data[block]:
		featVect[i][j] = feature
		j += 1
		if (j == nFeats):
			j = 0
			i += 1
