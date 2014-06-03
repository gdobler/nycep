import os

def nycep_extract_nyc_acs(year=2012, summary=1, dpath=None):
    """ Extract the NYC files from the full ACS data """

    # -- utilities
    if dpath==None:
        print("Must set data path to ACS data!")
    fbase = str(year)+str(summary)+'ny'
    gfile = 'g'+fbase+'.csv'


    # -- get the file list
    mlist = sorted([i for i in os.listdir(dpath) if 'm'+fbase in i])
    elist = sorted([i for i in os.listdir(dpath) if 'e'+fbase in i])


    # -- extract NYC Logical Record Numbers for NYC
    fopen   = open(os.path.join(dpath,gfile),'r')
    logrecn = [line.split(',')[4] for line in fopen if 'NYC' in line]
    fopen.close()


    # -- pull out only lines within NYC
    nfiles = len(mlist)
    lines  = []
    for ii,tfile in enumerate(mlist):
        print("working on file {0} of {1}...".format(ii+1,nfiles))
        lines += [line for line in open(os.path.join(dpath,tfile),'r') 
                  if line[25:32] in logrecn]


    return lines


if __name__=='__main__':

    dpath1 = '/home/gdobler/data/acs/2012/1'
    lines1 = nycep_extract_nyc_acs(dpath=dpath1,summary=1)
    opath1 = '../output/acs/2012/1'
    ofile1 = 'acs_nyc_2012_1.csv'
    print("writing file {0}...".format(os.path.join(opath1,ofile1)))
    fopen  = open(os.path.join(opath1,ofile1),'w')
    for line in lines1:
        fopen.write(line)
    fopen.close()

    dpath3 = '/home/gdobler/data/acs/2012/3'
    lines3 = nycep_extract_nyc_acs(dpath=dpath3,summary=3)
    opath3 = '../output/acs/2012/3'
    ofile3 = 'acs_nyc_2012_3.csv'
    print("writing file {0}...".format(os.path.join(opath3,ofile3)))
    fopen  = open(os.path.join(opath3,ofile3),'w')
    for line in lines3:
        fopen.write(line)
    fopen.close()
