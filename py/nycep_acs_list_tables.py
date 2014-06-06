import os

# -------- 
#  List the tables in the ACS data
#
#  Example:
#    year = 2012
#    summary = 5
#    dpath = '../../data/acs'
#    nycep_acs_list_tables(year=year, summary=summary, dpath=dpath)
#
#  2014/05/06 - Written by Greg Dobler (CUSP/NYU)
# -------- 
def nycep_acs_list_tables(year=2012, summary=1, dpath=None):
    """ List the tables in ACS data """

    # -- utilities
    if dpath==None:
        print("Must set data path to ACS data!")
        return
    path  = os.path.join(dpath,str(year),str(summary))
    sname = 'Sequence_Number_and_Table_Number_Lookup.txt'


    # -- read in the sequence #, table #, and names
    fopen = open(os.path.join(path,sname),'r')
    lines = [line for line in fopen if 'CELL' in line]
    fopen.close()


    # -- pull out the names
    tlabels = [line.split(',')[1] for line in lines]
    tnames  = [line.split(',')[-2] if '\"' not in line else 
               line.split('\"')[1] for line in lines]


    # -- write to file
    ofile = os.path.join('../output/acs',str(year),str(summary), 
                              'table_names.txt')
    print("writing table names to {0}".format(ofile))

    fopen = open(ofile,'w')
    [fopen.write("{0:10s}".format(i)+j+'\n') for i,j in zip(tlabels,tnames)]
    fopen.close()

    return
