import csv
import numpy as np
import collections
from sklearn.cluster import KMeans
import geopandas as gp
import matplotlib as plt
from pylab import *
import copy

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

addYear("../output/zbp/00totals.txt", emp, 3)
addYear("../output/zbp/01totals.txt", emp, 3)
addYear("../output/zbp/02totals.txt", emp, 3)
addYear("../output/zbp/03totals.txt", emp, 3)
addYear("../output/zbp/04totals.txt", emp, 3)
addYear("../output/zbp/05totals.txt", emp, 3)
addYear("../output/zbp/06totals.txt", emp, 3)
addYear("../output/zbp/07totals.txt", emp, 4)
addYear("../output/zbp/08totals.txt", emp, 4)
addYear("../output/zbp/09totals.txt", emp, 4)
addYear("../output/zbp/10totals.txt", emp, 4)
addYear("../output/zbp/11totals.txt", emp, 4)
addYear("../output/zbp/12totals.txt", emp, 4)

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
gfv = np.zeros(shape = (len(zcta), 13))
for zipCode in ordered:
	for j in range(0, 13):
		gfv[i][j] = emp[zipCode][j]
	i += 1

# taking only 2000-2012:
#gfv = copy.deepcopy(kfv)
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


# create geodataframe of different classes:
#gdf = gp.GeoDataFrame.from_file('../output/nyc-zip-code-extend.json')
gdf = gp.GeoDataFrame.from_file('../data/nyc_zipcta/nyc_zipcta.shp')

# dictionary of cluster labels for each zip code
labels = {}
for i in range(0, len(zcta)):
	labels[zcta[i]] = kmeans.labels_[i]

# for reference, create a list of zip codes that are not in both
# kmeans.labels_ and the geodataframe "zips"
noncommonZips = []
#fvzips = gdf['ZIP']
fvzips = gdf['ZCTA5CE00']
fvzips2 = []
for entry in fvzips:
	fvzips2.append(int(entry))
for entry in fvzips2:
	if entry not in zcta:
		if entry not in noncommonZips:
			noncommonZips.append(entry)
for entry in zcta:
	if int(entry) not in fvzips2:
		if entry not in noncommonZips:
			noncommonZips.append(entry)

# add "clusterLabels" to existing gdf
labelList = []
zipList = []
for i in range(0, len(gdf)):
#	geozip = int(gdf.loc[i].ZIP)
	geozip = int(gdf.loc[i].ZCTA5CE00)
	try:
		labelList.append(labels[geozip])
		zipList.append(geozip)
	except:
		labelList.append(-1)
		zipList.append(geozip)

gdf['clusterLabel'] = labelList

#figure()
#gdf.plot(column='clusterLabel', colormap='Accent')

gdf.to_file('../output/clusterPlots/shapefiles/employeesZip.shp')


# sum(kmeans.labels_==0)
# 0: 29
# 1: 22
# 2: 35
# 3: 61
# 4: 63

