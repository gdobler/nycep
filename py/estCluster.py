import csv
import numpy as np
import collections
from sklearn.cluster import KMeans
import geopandas as gp
import copy
import matplotlib.pyplot as plt

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
#fv = copy.deepcopy(fv[:,:])
fv = (fv.T - fv.mean(1)).T
fv = (fv.T/fv.std(1)).T

# generate n=5 clusters
kmeans = KMeans(init='random', n_clusters=5, n_init=10)
kmeans.fit(fv)


# create plots of five classes on one figure:
xlabels = ['00','02','04','06','08','10','12']

fig = figure()

ax1 = subplot(322)
ind = 0
ax1.set_xticklabels(xlabels)
ax1.get_yaxis().set_ticks([])
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='red')
ax1 = subplot(322)

ax2 = subplot(323)
ind = 1
ax2.set_xticklabels(xlabels)
ax2.get_yaxis().set_ticks([])
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='cyan')
ax2 = subplot(323)

ax3 = subplot(324)
ind = 2
ax3.set_xticklabels(xlabels)
ax3.get_yaxis().set_ticks([])
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='green')
ax3 = subplot(324)

ax4 = subplot(325)
ind = 3
ax4.set_xticklabels(xlabels)
ax4.get_yaxis().set_ticks([])
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='orange')
ax4 = subplot(325)

ax5 = subplot(326)
ind = 4
ax5.set_xticklabels(xlabels)
ax5.get_yaxis().set_ticks([])
plot(fv[kmeans.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans.cluster_centers_.T[:,ind],lw=2,color='#4B088A')
ax5 = subplot(326)

text(-14.5, 10.5, 'Total Number of \n Establishments\n k = 5', size=16)

# save plot to pdf:
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('estK5.pdf')
plt.savefig(pp, format='pdf')
pp.close()


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



# SECOND ROUND: K = 2
kmeans2 = KMeans(init='random', n_clusters=2, n_init=10)
kmeans2.fit(fv)

# create plots of both classes on one figure:
fig = figure()

ax1 = subplot(211)
ind = 0
ax1.set_xticklabels(xlabels)
ax1.get_yaxis().set_ticks([])
plt.plot(fv[kmeans2.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans2.cluster_centers_.T[:,ind],lw=2,color='darkblue')
title('Total Number of Establishments, k = 2', size = 16)
ax1 = subplot(211)

ax2 = subplot(212)
ind = 1
ax2.set_xticklabels(xlabels)
ax2.get_yaxis().set_ticks([])
plot(fv[kmeans2.labels_==ind].T,lw=0.5,color='grey')
plot(kmeans2.cluster_centers_.T[:,ind],lw=2,color='darkorange')
ax2 = subplot(212)

# save plot to pdf:
pp = PdfPages('estK2.pdf')
plt.savefig(pp, format='pdf')
pp.close()

# create geodataframe of different classes:
#gdf = gp.GeoDataFrame.from_file('../output/nyc-zip-code-extend.json')
gdf2 = gp.GeoDataFrame.from_file('../data/nyc_zipcta/nyc_zipcta.shp')

# dictionary of cluster labels for each zip code
labels = {}
for i in range(0, len(zcta)):
	labels[zcta[i]] = kmeans2.labels_[i]

# add "clusterLabels" to existing gdf
labelList = []
zipList = []
for i in range(0, len(gdf2)):
	geozip = int(gdf2.loc[i].ZCTA5CE00)
	try:
		labelList.append(labels[geozip])
		zipList.append(geozip)
	except:
		labelList.append(-1)
		zipList.append(geozip)

gdf2['clusterLabel'] = labelList

#figure()
#gdf.plot(column='clusterLabel', colormap='Accent')

# save gdf to shapefile for qgis
gdf2.to_file('../output/clusterPlots/shapefiles/estK2.shp')




