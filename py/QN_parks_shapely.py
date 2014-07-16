from shapely.geometry import Point
import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import isnan
import matplotlib.pyplot as plt

#Queens
try:
        QN
        Parks
except:
        QN = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\QN_joined_MV.csv')
        Parks= pkl.load(open('C:\\Users\\Acer\\nycep\\data\\Parks\\parks_polygons_parks_only.pkl'))

distQN = []
unitsQN = []
mvalQN=[]
sqfootQN=[]
indQN=[]

for i in range(len(QN)):
        use = QN['LandUse'][i]
        numunits=QN['UnitsRes'][i]
        mv=QN['Market_Val'][i]
        sqft=QN['BldgArea'][i]
        if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
                continue
        otx, oty = QN['XCoord'][i], QN['YCoord'][i]
        if isnan(otx) or (np.abs(otx)<1e-5):
                continue
        if isnan(mv) or (np.abs(mv)<1e-5):
                continue
        if isnan(sqft) or (np.abs(sqft)<1e-5):
                continue
        if i%10==0:
        	print "Completed", i, "out of", len(QN)
        tdist=[Point(otx, oty).distance(j) for j in Parks]
        mdist=min(tdist)
        distQN.append(mdist)
       	indQN.append(tdist.index(mdist))
        unitsQN.append(numunits)
        mvalQN.append(mv)
        sqfootQN.append(sqft)
distQN = np.array(distQN)
unitsQN = np.array(unitsQN)
mvalQN = np.array(mvalQN)
sqfootQN = np.array(sqfootQN)
indQN = np.array(indQN)
print mvalQN[0:100]
print distQN[0:100]
print indQN[0:100]


# #Histogram
# plt.hist(distQN,bins=100,range=(0,5000))
# plt.title('Queens Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()


# plt.hist(distQN, bins=100, range=(0,5000), weights=unitsQN)
# plt.title('Queens Units and their Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()


# plt.hist(mvalQN,bins=100, range=(0,2000000))
# plt.title('Queens Market Values')
# plt.ylabel('Frequency')
# plt.xlabel('Market Value')
# plt.show()
