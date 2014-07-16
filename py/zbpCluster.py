import csv
import numpy as np
import collections

# dictionary with zip code as key, list of total employees as value
emp = {}

# add all of the values for a yea to the dictionary
def addYear(fileName, dictionary):
	with open(fileName, "rU") as f:
		rows = csv.reader(f, delimiter = ",")
		rows.next()
		for row in rows:
			zc = row[0]
			if not zc in dictionary:
				dictionary[zc] = [float(row[4])]
			else:
				dictionary[zc].append(float(row[4]))

addYear("../output/zbp/12totals.txt", emp)
addYear("../output/zbp/11totals.txt", emp)
addYear("../output/zbp/10totals.txt", emp)
addYear("../output/zbp/09totals.txt", emp)
addYear("../output/zbp/08totals.txt", emp)
addYear("../output/zbp/07totals.txt", emp)
addYear("../output/zbp/06totals.txt", emp)
addYear("../output/zbp/05totals.txt", emp)
addYear("../output/zbp/04totals.txt", emp)
addYear("../output/zbp/03totals.txt", emp)
addYear("../output/zbp/02totals.txt", emp)
addYear("../output/zbp/01totals.txt", emp)
addYear("../output/zbp/00totals.txt", emp)
addYear("../output/zbp/99totals.txt", emp)
addYear("../output/zbp/98totals.txt", emp)
addYear("../output/zbp/97totals.txt", emp)
addYear("../output/zbp/96totals.txt", emp)
addYear("../output/zbp/95totals.txt", emp)
addYear("../output/zbp/94totals.txt", emp)

# 5 zip codes with missing entries are removed and ignored
ignore = ['10065', '10069', '11109', '11425', '10075']
for zipCode in ignore:
	del emp[zipCode]

# Get sorted array of NYC Zip Codes and remove above zip codes:
zcta = []
with open("../output/zbp/zcta.txt") as f:
	for line in f:
		zcta.append(int(line))
zcta.sort()
for zipCode in ignore:
	try:
		zcta.remove(int(zipCode))
	except:
		continue

# Create ordered dictionary of employment data 
ordered = collections.OrderedDict(sorted(emp.items()))

# Create numpy array of feature vectors that is consistent with the
# ordered list of zip codes.
i = 0
fv = np.zeros(shape = (len(ordered), 19))
for zipCode in ordered:
	for j in range(0, 19):
		fv[i][j] = emp[zipCode][j]
	i += 1

# still to do: generate clusters from numpy array "fv"


