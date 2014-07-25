import csv
import numpy as np
import geopandas as gp
from sklearn.cluster import KMeans
import math

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

kfv = np.zeros(shape = (nBlocks, nFeats))

i = 0
j = 0
for block in data:
	for feature in data[block]:
		feature = float(feature)
		if math.isnan(feature) or math.isinf(feature):
			print 'hi'
			kfv[i][j] = 0
		else:
			kfv[i][j] = feature
		j += 1
		if (j == nFeats):
			j = 0
			i += 1

# normalize featVect
nkfv = kfv
i = 0
j = 0
for line in kfv:
	mean = np.mean(line)
	stdev = np.std(line)
	for feature in line:
		feature -= mean
		feature /= stdev
		if math.isnan(feature):
			nkfv[i][j] = 0
		else:
			nkfv[i][j] = feature
		j += 1
	i +=1
	j = 0



# generate n clusters
n = 5
kmeans = KMeans(init='random', n_clusters = n, n_init = 10)
kmeans.fit(nkfv)

ind = 0
plot(nkfv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='maroon')

