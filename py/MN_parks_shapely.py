from shapely.geometry import Point
import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import isnan
import matplotlib.pyplot as plt

#Manhattan
try:
        MN
        Parks
except:
        MN = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\MN_joined_MV.csv')
        Parks= pkl.load(open('C:\\Users\\Acer\\nycep\\data\\Parks\\parks_polygons_parks_only.pkl'))

distMN = []
unitsMN = []
mvalMN=[]
sqfootMN=[]
indMN=[]

for i in range(len(MN)):
        use = MN['LandUse'][i]
        numunits=MN['UnitsRes'][i]
        mv=MN['Market_Val'][i]
        sqftMN=MN['BldgArea'][i]
        if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
                continue
        otx, oty = MN['XCoord'][i], MN['YCoord'][i]
        if isnan(otx) or (np.abs(otx)<1e-5):
                continue
        if isnan(mv) or (np.abs(mv)<1e-5):
                continue
        if isnan(sqftMN) or (np.abs(sqftMN)<1e-5):
                #print "sqft"
                continue
       	if i%10==0:
        	print "Completed", i, "out of", len(MN)
        tdist=[Point(otx, oty).distance(j) for j in Parks]
        mdist=min(tdist)
        distMN.append(mdist)
       	indMN.append(tdist.index(mdist))
        unitsMN.append(numunits)
        mvalMN.append(mv)
        sqfootMN.append(sqftMN)
distMN = np.array(distMN)
unitsMN = np.array(unitsMN)
mvalMN = np.array(mvalMN)
sqfootMN = np.array(sqfootMN)
indMN = np.array(indMN)
print mvMN[0:100]
print distMN[0:100]
print indMN[0:100]

#Histogram

# plt.hist(distMN,bins=100)
# plt.title('Manhattan Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()

# plt.hist(distMN, bins=100, range=(0,5000), weights=unitsMN)
# plt.title('Manhattan Units and their Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()

# plt.hist(mvalMN,bins=100, range=(0,12000000))
# plt.title('Manhattan Market Values')
# plt.ylabel('Frequency')
# plt.xlabel('Market Value')
# plt.show()


