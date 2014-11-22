import geopandas as gp
from geopandas import GeoSeries
import pandas as pd
import os
import sys
import csv
import numpy as np

#paramaters
parks = gp.GeoDataFrame.from_file('Parks_GreenSpace.shp')
geos = gp.GeoDataFrame.from_file('Counties_Clipped.shp')
zipsGeo = gp.GeoDataFrame.from_file('Zip_Codes.shp')
censustract = gp.GeoDataFrame.from_file('Census_Tracts_Clipped.shp')
pluto = gp.GeoDataFrame.from_file('PLUTO_TaxLots.shp')
Output = 'PLUTO_Joined_Distances'



#Match the projection of geos to parks
geos.to_crs(crs=(parks['geometry'].crs), inplace=True)
zipsGeo.to_crs(crs=(parks['geometry'].crs), inplace=True)
censustract.to_crs(crs=(parks['geometry'].crs), inplace=True)
pluto.to_crs(crs=(parks['geometry'].crs), inplace=True)

#Compute associated Geo IDs 
geos_geoid = np.array(geos['GEOID'])
zipsGeo_geoid = np.array(zipsGeo['ZCTA5CE10'])
censustract_geoid = np.array(censustract['GEOID'])


plGeo = np.zeros(len(pluto))
plZip = np.zeros(len(pluto))
plCT = np.zeros(len(pluto))


for jj, geo in enumerate(geos['geometry']):
	for ii, cen in enumerate(np.array(pluto.geometry.centroid)):
		if cen.within(geo):
			plGeoID = geos_geoid[jj]
			plGeo[ii] = plGeoID
pluto['Borough_ID'] = plGeo

for jj, geo in enumerate(zipsGeo['geometry']):
	for ii, cen in enumerate(np.array(pluto.geometry.centroid)):
		if cen.within(geo):
			plZipCode = zipsGeo_geoid[jj]
			plZip[ii] = plZipCode
pluto['ZipCode_PL'] = plZip

for jj, geo in enumerate(censustract['geometry']):
	for ii, cen in enumerate(np.array(pluto.geometry.centroid)):
		if cen.within(geo):
			plCenTr = censustract_geoid[jj]
			plCT[ii] = plCenTr
pluto['CensusTract_PL'] = plCT


#Calculate Min Distance from PLUTO Lot to Park

distplMin = np.zeros(len(pluto))

for ii, cen in enumerate(np.array(pluto.geometry.centroid)):
	if ii % 100 == 0:
		print "I am in ",ii
	tmin = 1e30
	for jj, park in enumerate(parks['geometry']):
		distpl = cen.distance(park)
		tmin = distpl if distpl < tmin else tmin
	distplMin[ii] = tmin
	#print distplMin

pluto['Dist_to_Closest_Park'] = distplMin
pluto.to_file(Output)

