"""
Awais Malik
Collaborated with Dr. Gregory Dobler
Histograms of Total Assessed Values for each borough
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Brooklyn
BK = pd.read_csv('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\data\\pluto\\BK.csv')
Assess_Tot = BK['AssessTot']
tot = np.array(Assess_Tot)
use = np.array(BK['LandUse'])
tot_trim = tot[(tot>0) & (use<4)] # Residential Buildings Only

plt.figure(1)
plt.hist(np.log10(1.0*tot_trim),bins=400,normed=True)
plt.title('Brooklyn Assessed Values')
#plt.ylabel('')
plt.xlabel('log$_1$$_0$(Total Assessed Value)')
#plt.figure(1).savefig('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\output\\pluto\\BK_AssessedValues.jpg',dpi = 500)

# Bronx
BX = pd.read_csv('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\data\\pluto\\BX.csv')
Assess_Tot1 = BX['AssessTot']
tot1 = np.array(Assess_Tot1)
use1 = np.array(BX['LandUse'])
tot_trim1 = tot1[tot1>0 & (use1<4)] # Residential Buildings Only

plt.figure(2)
plt.hist(np.log10(1.0*tot_trim1),bins=300,normed=True)
plt.title('Bronx Assessed Values')
#plt.ylabel('')
plt.xlabel('log$_1$$_0$(Total Assessed Value)')
#plt.figure(2).savefig('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\output\\pluto\\BX_AssessedValues.jpg',dpi = 500)

# Manhattan
MN = pd.read_csv('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\data\\pluto\\MN.csv')
Assess_Tot2 = MN['AssessTot']
tot2 = np.array(Assess_Tot2)
use2 = np.array(MN['LandUse'])
tot_trim2 = tot2[tot2>0 & (use2<4)] # Residential Buildings Only

plt.figure(3)
plt.hist(np.log10(1.0*tot_trim2),bins=200,normed=True)
plt.title('Manhattan Assessed Values')
#plt.ylabel('')
plt.xlabel('log$_1$$_0$(Total Assessed Value)')
#plt.figure(3).savefig('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\output\\pluto\\MN_AssessedValues.jpg',dpi = 500)

# Queens
QN = pd.read_csv('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\data\\pluto\\QN.csv')
Assess_Tot3 = QN['AssessTot']
tot3 = np.array(Assess_Tot3)
use3 = np.array(QN['LandUse'])
tot_trim3 = tot3[tot3>0 & (use3<4)] # Residential Buildings Only

plt.figure(4)
plt.hist(np.log10(1.0*tot_trim3),bins=450,normed=True)
plt.title('Queens Assessed Values')
#plt.ylabel('')
plt.xlabel('log$_1$$_0$(Total Assessed Value)')
#plt.figure(4).savefig('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\output\\pluto\\QN_AssessedValues.jpg',dpi = 500)

# Staten Island
SI = pd.read_csv('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\data\\pluto\\SI.csv')
Assess_Tot4 = SI['AssessTot']
tot4 = np.array(Assess_Tot4)
use4 = np.array(SI['LandUse'])
tot_trim4 = tot4[tot4>0 & (use4<4)] # Residential Buildings Only

plt.figure(5)
plt.hist(np.log10(1.0*tot_trim4),bins=350,normed=True)
plt.title('Staten Island Assessed Values')
#plt.ylabel('')
plt.xlabel('log$_1$$_0$(Total Assessed Value)')
#plt.figure(5).savefig('C:\\Users\\Awais\\Documents\\GitHub\\nycep\\output\\pluto\\SI_AssessedValues.jpg',dpi = 500)