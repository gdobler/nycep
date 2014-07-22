from shapely.geometry import Point
import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import isnan
import matplotlib.pyplot as plt

#Staten Island
try:
        SI
        Parks
except:
        SI = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\SI_joined_MV.csv')
        Parks= pkl.load(open('C:\\Users\\Acer\\nycep\\data\\Parks\\parks_polygons_parks_only.pkl'))

distSI = []
unitsSI = []
mvalSI=[]
sqfootSI=[]
indSI = []

for i in range(len(SI)):
        use = SI['LandUse'][i]
        numunits=SI['UnitsRes'][i]
        mv=SI['Market_Val'][i]
        sqft=SI['BldgArea'][i]
        if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
                continue
        otx, oty = SI['XCoord'][i], SI['YCoord'][i]
        if isnan(otx) or (np.abs(otx)<1e-5):
                continue
        if isnan(mv) or (np.abs(mv)<1e-5):
                continue
        if isnan(sqft) or (np.abs(sqft)<1e-5):
                continue
        if i%10==0:
        	print "Completed", i, "out of", len(SI)
        tdist=[Point(otx, oty).distance(j) for j in Parks]
        mdist=min(tdist)
        distSI.append(mdist)
       	indSI.append(tdist.index(mdist))
        unitsSI.append(numunits)
        mvalSI.append(mv)
        sqftSI.append(sqft)
distSI  = np.array(distSI)
unitsSI = np.array(unitsSI)
mvalSI = np.array(mvalSI)
sqfootSI = np.array(sqfootSI)
indSI = np.array(indSI)

print mvalSI[0:100]
print distSI[0:100]
print indSI[0:100]

# #Histogram
# plt.hist(distSI,bins=100,range=(0,5000))
# plt.title('Staten Island Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()


# plt.hist(distSI, bins=100, range=(0,5000), weights=unitsSI)
# plt.title('Staten Island Units and their Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()

# plt.hist(mvalSI,bins=100, range=(0,2000000))
# plt.title('Staten Island Market Values')
# plt.ylabel('Frequency')
# plt.xlabel('Market Value')
# plt.show()

# plt.plot(distSI, (mvalSI/sqfootSI), marker='o', linestyle="")
# # xlim=(0,2000000), ylim=(0,5000))
# plt.title('Staten Island Market Values vs. Distance from Park')
# plt.xlabel('Distance from Park')
# plt.ylabel('Market Value')
# plt.show()