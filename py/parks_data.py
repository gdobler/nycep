data = np.load("..npy")

always need to cut the pluto by landuse<4
dist=data.min(1)

ind=parks.area<.5
dist=data[:,ind].min(1)

cuts on area, and cuts on zipcode
in pluto there are zipcodes so look at distances to parks, small parks

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -- set input files                                                            
infile_pk = '../output/SI_parks_distances.npy'
infile_pl = '../data/pluto/SI.csv'
parks = pd.read_csv("C:\\Users\\Acer\\nycep\\output\\DPR_ParksProperties_001_nogeom.csv")

# -- load parks distances                                                       
pk = np.load(infile_pk)

# -- read PLUTO data and confine to land use 1 or 2                             
pl = pd.read_csv(infile_pl)
pl = pl[pl['LandUse']<3]

# -- plot a histogram for zipcode 10304                                         
ind  = np.array(pl['ZipCode']==10304)
dist = pk[ind].min(1)

plt.figure(0)
plt.grid(b=1)
plt.hist(dist,bins=100,range=[0,4000],facecolor='tan',edgecolor='darkred',
         normed=True)
plt.xlabel('distance to nearest park [ft]')
plt.ylabel('PDF')
plt.title('Staten Island')
plt.show()

