import os

# -------- 
#  Get a list of the logical record numbers for the census tracts in NYC
#
#  2014/06/06 - Written by Greg Dobler (CUSP/NYU)
# -------- 
def nycep_acs_tract_logrecno(dpath=None):

    # -- utilities
    if dpath==None:
        print('Must set data path!!!')
        return
    gfile = os.path.join(dpath,'2012','5','g20125ny.csv')
    burs  = ['Brooklyn','Bronx','Manhattan','Queens','Staten Island']

    # -- read in the geography file
    fopen = open(gfile,'r')
    lines = [line for line in fopen]
    fopen.close()


    # -- return only the logical record numbers from NYC
    return [line[16:23] for line in lines if 
            ('New York city' in line) and 
            ('Census Tract' in line)]
