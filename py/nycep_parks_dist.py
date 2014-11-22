import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import isnan
import matplotlib.pyplot as plt


# #Brooklyn
# try:
#         BK
# except:
#         BK = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\pluto\\BK.csv')

# grind = BK['LandUse']==9
# grx, gry = np.array(BK['XCoord'][grind]), np.array(BK['YCoord'][grind])
# #print grx, gry
# for i in range(len(grx)):
#         #print "hi"
#         if isnan(grx[i]) or isnan(gry[i]):
#                 #print "hello"
#                 grx[i]=0
#                 gry[i]=0

# distBK = []
# unitsBK=[]

# for i in range(len(BK)):
#         use = BK['LandUse'][i]
#         numunits=BK['UnitsRes'][i]
#         if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
#                 continue
#         otx, oty = BK['XCoord'][i], BK['YCoord'][i]
#         if isnan(otx) or (np.abs(otx)<1e-5):
#                 continue
#         distBK.append(np.sqrt((grx-otx)**2 + (gry-oty)**2).min())
#         unitsBK.append(numunits)
# distBK = np.array(distBK)
# unitsBK = np.array(unitsBK)
# print distBK[0:100]

# # #Histogram
# # plt.hist(distBK,bins=100,range=(0,5000))
# # plt.title('Brooklyn Distance to Parks')
# # plt.ylabel('Frequency')
# # plt.xlabel('Distance to Parks (feet)')
# # plt.show()

# plt.hist(distBK, bins=100, range=(0,5000), weights=units)
# plt.title('Brooklyn Units and their Distance to Parks')
# plt.ylabel('Frequency')
# plt.xlabel('Distance to Parks (feet)')
# plt.show()

# #Manhattan
# try:
#         MN
# except:
#         MN = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\pluto\\MN.csv')

# grind = MN['LandUse']==9
# grx, gry = np.array(MN['XCoord'][grind]), np.array(MN['YCoord'][grind])
# #print grx, gry
# for i in range(len(grx)):
#         #print "hi"
#         if isnan(grx[i]) or isnan(gry[i]):
#                 #print "hello"
#                 grx[i]=0
#                 gry[i]=0

# distMN = []
# unitsMN = []


# for i in range(len(MN)):
#         use = MN['LandUse'][i]
#         numunits=MN['UnitsRes'][i]
#         if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
#                 continue
#         otx, oty = MN['XCoord'][i], MN['YCoord'][i]
#         if isnan(otx) or (np.abs(otx)<1e-5):
#                 continue
#         distMN.append(np.sqrt((grx-otx)**2 + (gry-oty)**2).min())
#         unitsMN.append(numunits)
# distMN = np.array(distMN)
# unitsMN = np.array(unitsMN)
# print distMN[0:100]
# #Histogram

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

# #Bronx
# try:
#         BX
# except:
#         BX = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\pluto\\BX.csv')

# grind = BX['LandUse']==9
# grx, gry = np.array(BX['XCoord'][grind]), np.array(BX['YCoord'][grind])
# #print grx, gry
# for i in range(len(grx)):
#         #print "hi"
#         if isnan(grx[i]) or isnan(gry[i]):
#                 #print "hello"
#                 grx[i]=0
#                 gry[i]=0

# distBX = []
# unitsBX = []


# for i in range(len(BX)):
#         use = BX['LandUse'][i]
#         numunits=BX['UnitsRes'][i]
#         if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
#                 continue
#         otx, oty = BX['XCoord'][i], BX['YCoord'][i]
#         if isnan(otx) or (np.abs(otx)<1e-5):
#                 continue
#         distBX.append(np.sqrt((grx-otx)**2 + (gry-oty)**2).min())
#         unitsBX.append(numunits)
# distBX = np.array(distBX)
# unitsBX = np.array(unitsBX)

# print distBX[0:100]

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

# #Queens
# try:
#         QN
# except:
#         QN = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\pluto\\QN.csv')

# grind = QN['LandUse']==9
# grx, gry = np.array(QN['XCoord'][grind]), np.array(QN['YCoord'][grind])
# #print grx, gry
# for i in range(len(grx)):
#         #print "hi"
#         if isnan(grx[i]) or isnan(gry[i]):
#                 #print "hello"
#                 grx[i]=0
#                 gry[i]=0

# distQN = []
# unitsQN = []

# for i in range(len(QN)):
#         use = QN['LandUse'][i]
#         numunits=QN['UnitsRes'][i]
#         if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
#                 continue
#         otx, oty = QN['XCoord'][i], QN['YCoord'][i]
#         if isnan(otx) or (np.abs(otx)<1e-5):
#                 continue
#         distQN.append(np.sqrt((grx-otx)**2 + (gry-oty)**2).min())
#         unitsQN.append(numunits)
# distQN = np.array(distQN)
# unitsQN = np.array(unitsQN)
# print distQN[0:100]

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

#Staten Island
try:
        SI
except:
        SI = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\pluto\\SI.csv')

grind = SI['LandUse']==9
grx, gry = np.array(SI['XCoord'][grind]), np.array(SI['YCoord'][grind])
#print grx, gry
for i in range(len(grx)):
        #print "hi"
        if isnan(grx[i]) or isnan(gry[i]):
                #print "hello"
                grx[i]=0
                gry[i]=0

distSI = []
unitsSI = []

for i in range(len(SI)):
        use = SI['LandUse'][i]
        numunits=SI['UnitsRes'][i]
        if isnan(use) or (use==4) or (use==5) or (use==6) or (use==7) or (use==8) or (use==9):
                continue
        otx, oty = SI['XCoord'][i], SI['YCoord'][i]
        if isnan(otx) or (np.abs(otx)<1e-5):
                continue
        distSI.append(np.sqrt((grx-otx)**2 + (gry-oty)**2).min())
        unitsSI.append(numunits)
distSI  = np.array(distSI)
unitsSI = np.array(unitsSI)
print distSI[0:100]

#Histogram
plt.hist(distSI,bins=100,range=(0,5000))
plt.title('Staten Island Distance to Parks')
plt.ylabel('Frequency')
plt.xlabel('Distance to Parks (feet)')
plt.show()


plt.hist(distSI, bins=100, range=(0,5000), weights=unitsSI)
plt.title('Staten Island Units and their Distance to Parks')
plt.ylabel('Frequency')
plt.xlabel('Distance to Parks (feet)')
plt.show()

#pluto.csv
#awais.csv
# bbl-p,x,y=read(pluto.csv)
# bbl-a,mv=read(awais.csv)
# for each bbl-p
#         i where bbl-a==bbl-p
#         dict[bbl-p]=[x,y,mv[i]]

# #1395.0211467931231
#print list(dist).index(min(dist))
# #9
#print dist[9]
# #1395.0211467931231