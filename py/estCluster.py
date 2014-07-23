import csv
import numpy as np
import collections
from sklearn.cluster import KMeans
import geopandas as gp
import copy
import matplotlib as plt

# dictionary with zip code as key, list of total establishments as value
est = {}

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

addYear("../output/zbp/00totals.txt", est, 6)
addYear("../output/zbp/01totals.txt", est, 6)
addYear("../output/zbp/02totals.txt", est, 6)
addYear("../output/zbp/03totals.txt", est, 6)
addYear("../output/zbp/04totals.txt", est, 6)
addYear("../output/zbp/05totals.txt", est, 6)
addYear("../output/zbp/06totals.txt", est, 6)
addYear("../output/zbp/07totals.txt", est, 9)
addYear("../output/zbp/08totals.txt", est, 9)
addYear("../output/zbp/09totals.txt", est, 9)
addYear("../output/zbp/10totals.txt", est, 9)
addYear("../output/zbp/11totals.txt", est, 9)
addYear("../output/zbp/12totals.txt", est, 9)


# 5 zip codes with missing entries are removed and ignored
ignore = ['10065', '10069', '11109', '11425', '10075']
for zipCode in ignore:
	del est[zipCode]

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

nYears = len(est['10001'])

# Create ordered dictionary of establishments
oest = collections.OrderedDict(sorted(est.items()))

# Create numpy array of feature vectors that is consistent with the
# ordered list of zip codes.
i = 0
fv = np.zeros(shape = (len(oest), nYears))
for zipCode in oest:
	for j in range(0, nYears):
		fv[i][j] = est[zipCode][j]
	i += 1

# normalize feature vector
fv = copy.deepcopy(fv[:,:])
fv = (fv.T - fv.mean(1)).T
fv = (fv.T/fv.std(1)).T

# generate n=5 clusters
kmeans = KMeans(init='random', n_clusters=5, n_init=10)
kmeans.fit(fv)


# create plots of five classes on one figure:
fig = figure()

ind = 0
ax1 = fig.add_subplot(322)
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='maroon')

ind = 1
ax2 = fig.add_subplot(323)
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='blue')

ind = 2
ax3 = fig.add_subplot(324)
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='green')

ind = 3
ax4 = fig.add_subplot(325)
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='orange')

ind = 4
ax5 = fig.add_subplot(326)
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='purple')

text(-14.5, 14, 'Total Establishments\n k = 5', size=16)



# create geodataframe of different classes:
#gdf = gp.GeoDataFrame.from_file('../output/nyc-zip-code-extend.json')
gdf = gp.GeoDataFrame.from_file('../data/nyc_zipcta/nyc_zipcta.shp')

# dictionary of cluster labels for each zip code
labels = {}
for i in range(0, len(zcta)):
	labels[zcta[i]] = kmeans.labels_[i]


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

gdf.to_file('../output/clusterPlots/shapefiles/establishmentsZip.shp')



