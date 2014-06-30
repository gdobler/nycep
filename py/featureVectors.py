import csv
import numpy as np

data = {}

def addFeatures(fileName, dictionary):
	with open(fileName) as f:
		lines = csv.reader(f, delimiter = ",")
		lines.next()
		for line in lines:
			length = len(line)
			logrecno = line[0]
			if not logrecno in dictionary:
				for i in range(1, length):
					if (i == 1):
						dictionary[logrecno] = [line[1]]
					else:
						dictionary[logrecno].append(line[i])
			else:
				for i in range(1, length):
					dictionary[logrecno].append(line[i])

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

print nBlocks, nFeats

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


for line in featVect:
	print line
	break

