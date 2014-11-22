import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import isnan
import matplotlib.pyplot as plt
#from sql import *


#Brooklyn
try:
        BK
        BK_MV
except:
        BK = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\pluto\\BK.csv')
        BK_MV = pd.read_csv('C:\\Users\\Acer\\nycep\\data\\MarketValues\\Brooklyn.csv')

mydict = {}
for x in range(len(BK)):
    currentid = BK.iloc[x,0]
    currentvalue = BK.iloc[x,1]
    mydict.setdefault(currentid, [])
    mydict[currentid].append(currentvalue)

#pd.DataFrame.set_index(BK).to_dict()


#BK=pd.DataFrame({'BBL':BBL, 'XCoord':XCoord, 'YCoord':YCoord,'UnitsRes':UnitsRes})

#merge(BK,BK_MV, left_on="BBL", right_index=True, how="inner")

#new=BK.join(BK_MV,on="BBL",how="inner",lsuffix='_left',rsuffix= '_right')
#new=merge(BK,BK_MV, on='BBL',suffixes=['_left','_right'])

#print new[1:10]

# join1=BBL.join(BK('BBL'))
# join2=join1.join(Table('BBLE'))
# select=join2.select(BBL)
# BBL=BK['BBL']
# BBLE=BK_MV['BBLE']
# BBLt={}

# for i in range(len(BK)):
# 	if BBL[i]==BK_MV['BBLE']:
#  		dict[BBLt]={x,y,Market_Value[i]}
