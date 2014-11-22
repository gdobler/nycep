import geopandas as gp
from geopandas import GeoSeries
import pandas as pd
import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import itertools
from itertools import cycle, islice
#paramaters

parks = gp.GeoDataFrame.from_file('C:\Users\Amanda\NYC_Raw\Parks_GreenSpace.shp')
geos = gp.GeoDataFrame.from_file('C:\Users\Amanda\NYC_Raw\Counties_Clipped.shp')
population = 'C:\NYU\GRA\Data\Raw\Population_Data\Counties\ACS_12_5YR_B01003_with_ann.csv'
Output = 'C:\NYU\GRA\Data\Output_Shapefiles\Counties_Pop_Fraction'

##csvfile = open(population, 'r')
##reader = csv.reader(csvfile)
##next(reader,None)


pop_pd = pd.read_csv(population)
#geos_zip = np.array(geos['GEOID'])
#check = []

#for i in pop_pd['Id2'].astype(str):
#	if i in geos_zip:
#		check.append(i)
#		print "TRUE"

		
zips_geo = np.array(geos['GEOID'])
zips_pop = list(pop_pd['Id2'].astype(str))
pop_pop = np.array(pop_pd['Estimate; Total'])
pop_geo = np.zeros(len(zips_geo))

for ii,zz in enumerate(zips_geo):
	pop_geo[ii] = pop_pop[zips_pop.index(zz)]


##for row in reader:
##	zips_pop = (row[1])                 
##for ii,zz in enumerate(zips_geo):
##	#print ii
##	ind = zips_pop.index(ii)
##	Pop_geo(zz) = reader(ind)
##
##
##
###Match the projection of geos to parks
geos.to_crs(crs=(parks['geometry'].crs), inplace=True)
##
#Calculate percent area of geos that are parks
total_parks_area = np.zeros(len(geos))

for jj, park in enumerate(parks['geometry']):
    if jj % 100 == 0:
        print "I am in ",jj
    for ii, geo in enumerate(geos['geometry']):
##        #ratio = ((intersection(parks, geos).area)/park.area)
        ratio = geo.intersection(park).area/park.area
       
        total_parks_area[ii] += ratio*park.area
fraction = total_parks_area/geos.area
pop_fraction = total_parks_area/pop_geo


#Write fration to file
geos['Parks_Fraction'] = fraction
geos['Total_Park_Area'] = total_parks_area
geos['Population'] = pop_geo
geos['Area_Park_perPerson'] = pop_fraction

geos.to_file(Output)


my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(d)))
plt.xlabel('County')
plt.ylabel('Area of Park Space per Person in sf')
plt.title('Area of Park Space per Person in sf by County in NYC')
plt.bar(range(len(d)), d.values(), align='center', color=my_colors)
plt.xticks(range(len(d)), d.keys())
plt.show()