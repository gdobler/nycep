import os
import numpy as np
import geopandas as gp

# -------- 
#  Load in the parks shape file and write to csv
#
#  2014/07/21 - Written by Greg Dobler (CUSP/NYU)
# -------- 

def nycep_parks_shp2csv(dpath='../data/Parks/DPR_ParksProperties_001', 
                        infile='DPR_ParksProperties_001.shp',
                        opath='../output', 
                        ofile='DPR_ParksProperties_001_nogeom.csv'):

    # -- read in the shape file
    shp = gp.GeoDataFrame.from_file(os.path.join(dpath,infile)
                                    ).drop('geometry',1)
    shp.to_csv(os.path.join(opath,ofile),encoding='utf-8')

    return


if __name__=='__main__':

    nycep_parks_shp2csv()
