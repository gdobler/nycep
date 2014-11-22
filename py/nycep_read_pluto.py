import os, sys
import numpy as np
import matplotlib.pyplot as plt

# -- set the burrough
bur = 'MN'


# -- get the input data file
print("Reading the data for {0}...".format(bur))
dpath = '../data/pluto'
dfile = os.path.join(dpath,bur+'.csv')
lines = [line for line in open(dfile,'r')]


# -- get x and y indices
xind = lines[0].split(',').index('XCoord')
yind = lines[0].split(',').index('YCoord')
aind = lines[0].split(',').index('AssessTot')


# -- break off X, Y, and Assessed Total Value
print("Grabbing position and total assessed value...")
xarr_full = np.zeros(len(lines)-1)
yarr_full = np.zeros(len(lines)-1)
aarr_full = np.zeros(len(lines)-1)

for ii,line in enumerate(lines[1:]):
    vals = line.split(',')
    xval = vals[xind]
    yval = vals[yind]
    aval = vals[aind]
    if len(xval)>0:
        xarr_full[ii] = float(xval)
    if len(yval)>0:
        yarr_full[ii] = float(yval)
    if len(aval)>0:
        aarr_full[ii] = float(aval)


# -- do a bit of cleaning
print("Cleaning...")
gpix = (xarr_full>800000) & (xarr_full<2000000) & (aarr_full>0.0)
xarr = xarr_full[gpix]/1e4
yarr = yarr_full[gpix]/1e4
aarr = np.log10(aarr_full[gpix])


# -- set up the scatter plot colors
amx   = aarr.max()
amn   = aarr.min()
alpha = (0.9*(aarr - amn)/(amx-amn) + 0.1).clip(0.1,1.0)
color = np.array([[0.5,i,i**2,i] for i in alpha])


# -- plot it
print("Plotting...")
plt.figure(1)
plt.clf()
plt.ylim([19,27])
plt.xlim([95,103])
plt.scatter(xarr,yarr,s=5,c=color,linewidths=0)
plt.savefig('../output/assess_val_'+bur+'.pdf',clobber=True)
plt.close()
