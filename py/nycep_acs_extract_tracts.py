import os
from nycep_acs_tract_logrecno import *

# -------- 
#  Extract only the NYC census tracts from the estimates and margins files
#
#
#  2014/06/06 - Written by Greg Dobler (CUSP/NYU)
# -------- 

def nycep_acs_extract_tracts(dpath=None):

    # -- defaults
    if dpath==None:
        print("Must set ACS data path!!!")
        return
    d5path = os.path.join(dpath,'2012','5')


    # -- utilities
    opath = os.path.join('../output','acs','2012','5')


    # -- get the file list
    flist = sorted([i for i in os.listdir(d5path) if '000.txt' in i])


    # -- get the Logical Record Numbers for NYC census tracts
    logrecno = nycep_acs_tract_logrecno(dpath=dpath)


    # -- loop through the files and extract the appropriate lines
    for fl in flist:
        in_file  = open(os.path.join(d5path,fl),'r')
        out_file = open(os.path.join(opath,fl),'w')

        print("Writing file {0}...".format(os.path.join(opath,fl)))

        dum = [out_file.write(i) for i in in_file if 
               i.split(',')[5] in logrecno]

        in_file.close()
        out_file.close()

    return

nycep_acs_extract_tracts(dpath='../../data/acs')
