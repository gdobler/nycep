from shapely.geometry import Point
import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import isnan
import matplotlib.pyplot as plt

#Brooklyn
try:
        BK
        Parks
except:
        BK = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\BK_joined_MV.csv')
        Parks= pkl.load(open('C:\\Users\\Acer\\nycep\\data\\Parks\\parks_polygons_parks_only.pkl'))

distBK = []
unitsBK=[]
mvalBK=[]
sqfootBK=[]
indBK=[]


for i in range(len(BK)):
        use = BK['LandUse'][i]
        numunits=BK['UnitsRes'][i]
        mv=BK['Market_Value'][i]
        sqftBK=BK['BldgArea'][i]
        if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
                continue
       	if isnan(mv) or (np.abs(mv)<1e-5):
                continue
        otx, oty = BK['XCoord'][i], BK['YCoord'][i]
        if isnan(otx) or (np.abs(otx)<1e-5):
                continue
        if isnan(sqftBK) or (np.abs(sqftBK)<1e-5):
                #print "sqft"
                continue
        if i%10==0:
            print "Completed", i, "out of", len(BK)
        tdist=[Point(otx, oty).distance(j) for j in Parks]
        mdist=min(tdist)
        distBK.append(mdist)
        indBK.append(tdist.index(mdist))
        unitsBK.append(numunits)
        mvalBK.append(mv)
        sqfootBK.append(sqftBK)
distBK = np.array(distBK)
unitsBK = np.array(unitsBK)
mvalBK = np.array(mvalBK)
sqfootBK = np.array(sqfootBK)
indBK = np.array(indBK)

print distBK[0:100]
print distBK[0:100]
print indBK[0:100]
#Histogram
# plt.hist(distBK,bins=100,range=(0,5000))
# plt.title('Brooklyn Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()

# plt.hist(distBK, bins=100, range=(0,5000), weights=unitsBK)
# plt.title('Brooklyn Units and their Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()

# plt.hist(mvalBK,bins=100, range=(0,3500000))
# plt.title('Brooklyn Market Values')
# plt.ylabel('Frequency')
# plt.xlabel('Market Value')
# plt.show()
