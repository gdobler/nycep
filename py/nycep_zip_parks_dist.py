import os, sys
import numpy as np
import pandas as pd
import pickle as pkl

# -------- 
#  Determine the minimum distance array to (select) parks as a function of 
#  zipcode.
#
#  2014/08/06 - Written by Greg Dobler (CUSP/NYU)
# -------- 

def nycep_zip_parks_dist(bur,allparks=False):

    # -- get the distance file
    print("reading distances for {0}...".format(bur))
    dpath = '../output'
    dist = np.load(os.path.join(dpath,bur+'_parks_distances.npy'))


    # -- get PLUTO data
    print("reading pluto...")
    ppath = '../data/pluto'
    pl = pd.read_csv(os.path.join(ppath,bur+'.csv'))
    pl = pl[pl['LandUse']<4] # cut on residential properties


    # -- get the parks data
    print("reading parks data...")
    pkpath = '../output'
    parks = pd.read_csv(os.path.join(pkpath,
                                     'DPR_ParksProperties_001_nogeom.csv'))


    # -- set the index of appropriate parks
    if allparks:
        ind = np.arange(dist.shape[1])
    else:
        ind = np.array((parks['TYPECATEGO']!='Cemetery') & 
                       (parks['TYPECATEGO']!='Buildings/Institutions') & 
                       (parks['TYPECATEGO']!='Historic House Park') & 
                       (parks['TYPECATEGO']!='Undeveloped') & 
                       (parks['TYPECATEGO']!='Waterfront Facility'))


    # -- get array of minimum distances for zipcodes
    zips    = [i for i in set(pl['ZipCode']) if not np.isnan(i)]
    zip_dic = {}

    for ii,izip in enumerate(zips):
        print("generating minimium distances for " + 
              "{0} of {1}...\r".format(ii+1,len(zips))),
        sys.stdout.flush()
        zip_dic[izip] = (dist[np.array(pl['ZipCode']==izip),:][:,ind]
                         ).min(1)

    print("")


    # -- write to file
    opath   = '../output'
    ofile   = 'zip_min_park_dist_dic_{0}.pkl'.format(bur)
    outfile = os.path.join(opath,ofile)

    print("writing minimum distance dictionaries to {0}".format(outfile))
    pkl.dump(zip_dic,open(outfile,'wb'))

    return


if __name__=='__main__':

    burs = ['BK','BX','MN','QN','SI']

    for bur in burs:
        nycep_zip_parks_dist(bur)


