import csv
import numpy as np

data = {}

def addFeatures(fileName, dictionary):
	with open(fileName) as f:
		lines = csv.reader(f, delimiter = ",")
		lines.next()
		for line in lines:
			length = len(line)
			block = line[0]
			if not block in dictionary:
				dictionary[block] = [line[1:length]]
			else:
				dictionary[block].append(line[1:length])

addFeatures("../output/censusOutput/ageOfFemales.csv", data)
addFeatures("../output/censusOutput/ageOfMales.csv", data)
addFeatures("../output/censusOutput/avgHHSize.csv", data)
addFeatures("../output/censusOutput/ownerOccupied.csv", data)
addFeatures("../output/censusOutput/renterOccupied.csv", data)
addFeatures("../output/censusOutput/vacantHousingUnits.csv", data)

nBlocks = len(data)
nFeats = 0

for block in data:
	len1 = len(data[block])
	for features in data[block]:
		len2 = len(features)
		nFeats += len2
	break

featVect = np.zeros(shape = (nBlocks, nFeats))

i = 0
j = 0
for block in data:
	for features in data[block]:
		for attribute in features:
			featVect[i][j] = attribute
			if (j == nFeats):
				j = 0
			if (i == nBlocks): 
				break

for line in featVect:
	print line
	break