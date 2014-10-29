import geopandas as gp
from geopandas import GeoSeries
import os


#paramaters

parks = gp.GeoDataFrame.from_file('NYC_Raw/Parks_GreenSpace.shp')
geos = gp.GeoDataFrame.from_file('NYC_Raw/Zip_Codes.shp')
Output = 'C:\NYU\GRA\Zips_Parks_Fraction'

#Match the projection of geos to parks
geos.to_crs(crs=(parks['geometry'].crs), inplace=True)

#Calculate percent area of geos that are parks
total_parks_area = np.zeros(len(geos))

for jj, park in enumerate(parks['geometry']):
    if jj % 100 == 0:
        print "I am in ",jj
    for ii, geo in enumerate(geos['geometry']):
        #ratio = ((intersection(parks, geos).area)/park.area)
        ratio = geo.intersection(park).area/park.area
        
        total_parks_area[ii] += ratio*park.area
fraction = total_parks_area/geos.area

#Write fration to file
geos['Fraction_Parks'] = fraction
geos.to_file(Output)