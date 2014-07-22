import csv
import numpy as np
import collections
from sklearn.cluster import KMeans
import geopandas as gp
import copy
import matplotlib as plt

# dictionary with zip code as key, list of total employees as value
emp = {}

# add all of the values for a year to the dictionary
# add all of the values for a year to the dictionary
def addYear(fileName, dictionary, ind):
	with open(fileName, "rU") as f:
		rows = csv.reader(f, delimiter = ",")
		rows.next()
		for row in rows:
			zc = row[0]
			if not zc in dictionary:
				dictionary[zc] = [float(row[ind])]
			else:
				dictionary[zc].append(float(row[ind]))

addYear("../output/zbp/12totals.txt", emp, 4)
addYear("../output/zbp/11totals.txt", emp, 4)
addYear("../output/zbp/10totals.txt", emp, 4)
addYear("../output/zbp/09totals.txt", emp, 4)
addYear("../output/zbp/08totals.txt", emp, 4)
addYear("../output/zbp/07totals.txt", emp, 4)
addYear("../output/zbp/06totals.txt", emp, 3)
addYear("../output/zbp/05totals.txt", emp, 3)
addYear("../output/zbp/04totals.txt", emp, 3)
addYear("../output/zbp/03totals.txt", emp, 3)
addYear("../output/zbp/02totals.txt", emp, 3)
addYear("../output/zbp/01totals.txt", emp, 3)
addYear("../output/zbp/00totals.txt", emp, 3)
addYear("../output/zbp/99totals.txt", emp, 3)
addYear("../output/zbp/98totals.txt", emp, 3)
addYear("../output/zbp/97totals.txt", emp, 3)
addYear("../output/zbp/96totals.txt", emp, 3)
addYear("../output/zbp/95totals.txt", emp, 3)
addYear("../output/zbp/94totals.txt", emp, 3)

# 5 zip codes with missing entries are removed and ignored
ignore = ['10065', '10069', '11109', '11425', '10075']
for zipCode in ignore:
	del emp[zipCode]

# Get sorted array of NYC Zip Codes and remove above zip codes:
zcta = []
with open("../output/zbp/zcta.txt") as f:
	for line in f:
		zcta.append(int(line))
zcta.sort()
for zipCode in ignore:
	try:
		zcta.remove(int(zipCode))
	except:
		continue

# Create ordered dictionary of employment data 
ordered = collections.OrderedDict(sorted(emp.items()))

# Create numpy array of feature vectors that is consistent with the
# ordered list of zip codes.
i = 0
fv = np.zeros(shape = (len(ordered), 19))
for zipCode in ordered:
	for j in range(0, 19):
		fv[i][j] = emp[zipCode][j]
	i += 1

# normalize fv entries:
#fvNorm = np.zeros(shape = (len(ordered), 19))
#normVars = []
#for feature in fv:
#	std = np.std(feature)
#	mean = np.mean(feature)
#	normVars.append([mean, std])

#normalizedFV = fv

#for i in range(0, len(fv)):
#	for j in range(0, 19):
#		normalizedFV[i][j] = fv[i][j] - normVars[i][0]
#		normalizedFV[i][j] = fv[i][j] / normVars[i][1]


# taking only 2000-2012:
gfv = copy.deepcopy(fv[:,6:])
gfv = (gfv.T - gfv.mean(1)).T
gfv = (gfv.T/gfv.std(1)).T

# generate n=5 clusters
kmeans = KMeans(init='random', n_clusters=5, n_init=10)
kmeans.fit(gfv)


# create plots of five classes on one figure:
fig = figure()

ind = 0
ax1 = fig.add_subplot(322)
plot(gfv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='maroon')

ind = 1
ax2 = fig.add_subplot(323)
plot(gfv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='blue')

ind = 2
ax3 = fig.add_subplot(324)
plot(gfv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='green')

ind = 3
ax4 = fig.add_subplot(325)
plot(gfv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='orange')

ind = 4
ax5 = fig.add_subplot(326)
plot(gfv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='purple')

text(-14.5, 15, 'Total Number of Employees\n k = 5', size=16)


# create map of different classes:
zips = gp.GeoDataFrame.from_file('../data/nyc_zipcta/nyc_zipcta.shp')
#zips.plot()

# first need to filter out zip codes that don't appear in either
# geodataframe "zips" or in the feature vectors:
#noncommonZips = []
#fvzips = zips['ZCTA5CE00']
#fvzips2 = []
#for entry in fvzips:
#	fvzips2.append(int(entry))
#for entry in fvzips2:
#	if entry not in zcta:
#		if entry not in noncommonZips:
#			noncommonZips.append(entry)
#for entry in zcta:
#	if int(entry) not in fvzips2:
#		if entry not in noncommonZips:
#			noncommonZips.append(entry)

#dropThese = []
#for i in range(0, len(zips)):
#	zc = zips.loc[i].ZCTA5CE00
#	if int(zc) in noncommonZips:
#		dropThese.append(i)

#newgdf = zips.drop(dropThese)



#zips['cluster'] = -1

#clusterLabels = {}
#for i in range(0, len(zcta)):
#	zc = zcta[i]
#	label = kmeans.labels_[i]
#	clusterLabels[]
