import os

# -- utilities
burs  = ['BK','BX','MN','QN','SI']
dpath = '../data/pluto'
oname = 'pluto_all_buroughs.csv'
opath = '../output'
ofile = os.path.join(opath,oname)


# -- open the output file
fopen = open(ofile,'w')


# -- loop through buroughs and concatenate
for ii,bur in enumerate(burs):
    print('Reading burough {0}'.format(bur))

    infile = os.path.join(dpath,bur+'.csv')
    lines  = [line for line in open(infile,'r')][int(ii!=0):]

    print('Writing burough {0}...'.format(bur))
    for line in lines:
        fopen.write(line)


# -- close the output file
fopen.close()
