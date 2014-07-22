import numpy as py

# -- read in the areas file
lines = [line for line in open('../data/ParkInZip.csv')]


# -- loop through and create dictionary
dic = {}

for line in lines[1:]:
    reg     = line.split(',')
    zipcode = reg[0].zfill(5)
    area    = float(reg[1])
    pkarea  = float(reg[3])

    if zipcode in dic.keys():
        dic[zipcode][1] += pkarea
    else:
        dic[zipcode] = [area,pkarea]

keys = sorted(dic.keys())

fopen = open('../output/zips_park_pcnt.csv','w')
fopen.write('Zipcode,PercentParksCoverage\n')
for key in keys:
    fopen.write(key+','+str(dic[key][1]/dic[key][0])+'\n')
fopen.close()
