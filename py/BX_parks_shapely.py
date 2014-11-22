from shapely.geometry import Point
import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import isnan
import matplotlib.pyplot as plt

#Bronx
try:
        BX
        Parks
except:
        BX = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\BX_joined_MV.csv')
        Parks= pkl.load(open('C:\\Users\\Acer\\nycep\\data\\Parks\\parks_polygons_parks_only.pkl'))

distBX = []
unitsBX = []
mvalBX = []
sqfootBX = []
indBX=[]

#print this_point

for i in range(len(BX)):
        use = BX['LandUse'][i]
        numunits=BX['UnitsRes'][i]
        mv=BX['Market_Val'][i]
        sqftBX=BX['BldgArea'][i]
        if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
                continue
        otx,oty = BX['XCoord'][i], BX['YCoord'][i]
        if isnan(otx) or (np.abs(otx)<1e-5):
                continue
        if isnan(mv) or (np.abs(mv)<1e-5):
                continue
        if isnan(sqftBX) or (np.abs(sqftBX)<1e-5):
                #print "sqft"
                continue
       	if i%10==0:
        	print "Completed", i, "out of", len(BX)
        tdist=[Point(otx, oty).distance(j) for j in Parks]
        mdist=min(tdist)
        distBX.append(mdist)
       	indBX.append(tdist.index(mdist))
        unitsBX.append(numunits)
        mvalBX.append(mv)
        sqfootBX.append(sqftBX)
distBX = np.array(distBX)
unitsBX = np.array(unitsBX)
mvalBX = np.array(mvalBX)
sqfootBX = np.array(sqfootBX)
indBX = np.array(indBX)

print mvalBX[0:100]
print distBX[0:100]
print indBX[0:100]

# #Histogram
# plt.hist(distBX,bins=100,range=(0,5000))
# plt.title('Bronx Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()

# plt.hist(distBX, bins=100, range=(0,5000), weights=unitsBX)
# plt.title('Bronx Units and their Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()

# plt.hist(mvBX,bins=100, range=(0,2000000))
# plt.title('Bronx Market Values')
# plt.ylabel('Frequency')
# plt.xlabel('Market Value')
# plt.show()

