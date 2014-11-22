import numpy as np
import csv

# funtion to grab key value pairs from the xml file
def getKV(field):
	try:
		key, value = field.split("=")
	except:
		key, value = field, 0
	return key, value

# function to set values of park quality fields
# if the field is not present in xml file, value for
# that key is set to -1
def setFields(u, w, k, v, pA, eF):
	if extraFields[w] == k:
		parkArray[u][w] = v
	else:
		parkArray[u][w] = -1

xml = []
parks = {}
xmlArray = []

with open("../data/Parks/ParksFlat.txt", "r") as f:
	xml = f.readlines()

# create an array of just the key/value pairs in the file
for line in xml:
	line = line.strip()
	fields = line.split("/")
	fields.remove("")
	xmlArray.append(fields)

# if the line length is 3 then it corresponds to a new
# park ID in the file (based on the structure of the xml file)
# create a new dictionary with the park ID as the key
for line in xmlArray:
	if (len(line) == 3):
		tempId = line[2]
		idType, tempId = getKV(tempId)
		if idType.strip() == "ParkId":
			if tempId not in parks:
				parks[tempId] = []


extraFields = {5: "Glass", 6: "Graffiti", 7: "Litter", 8: "Weeds", 9: "Ice", 10: "Lawns", 11: "Trees", 12: "WaterBodies", 13: "HorticulturalAreas", 14: "AthleticFields", 15: "Trails", 16: "Benches", 17: "Fences", 18: "PavedSurfaces", 19: "PlayEquipment", 20: "SafetySurface", 21: "Sidewalks"}
numParks = len(parks)

parkArray = [[0 for col in range(6)] for row in range(numParks)]
parkId = False
i = 0
j = 0

for line in xmlArray:
	if parkId:
		if (j == 1):
			temp = line[2]
			siteName, name = getKV(temp)
			parkArray[i][j] = name
			j += 1
			continue
		elif (j == 2 or j == 3 or j == 4):
			temp = line[4]
			key, value = getKV(temp)
			parkArray[i][j] = value
#			if j == 4:
#				parkId = False
#				i += 1
#				continue
			j += 1
# IGNORE: attempt to add additional fields
		else:
			if j == 6:
				parkId = False
				i += 1
				continue
			try:
				temp = line[5]
				key, value = getKV(temp)
			except:
				key, value = 'junk', 'junk'
			setFields(i, j, key, value, parkArray, extraFields)
			j += 1
			continue
	else:
		if len(line) != 3:
			continue
		if i == numParks:
			break
		tempId = line[2]
		idType, tempId = getKV(tempId)
		parkArray[i][0] = tempId
		j = 1
		parkId = True

for entry in parkArray:
	if (entry[3] == 'Acceptable'):
		entry[3] = 1.0
	elif (entry[3] == 'Unacceptable'):
		entry[3] = 0.0
	elif (entry[3] == 'Not Rated'):
		entry[3] = -1

	if (entry[4] == 'Acceptable'):
		entry[4] = 1.0
	elif (entry[4] == 'Unacceptable'):
		entry[4] = 0.0
	elif (entry[4] == 'Not Rated'):
		entry[4] = -1	

	if (entry[5] == 'Acceptable'):
		entry[5] = 1.0
	elif (entry[5] == 'Unacceptable'):
		entry[5] = 0.0
	elif (entry[5] == 'Not Rated'):
		entry[5] = -1	


w = open("../data/Parks/ParksCSV.csv", "wb")
wr = csv.writer(w, delimiter = ",")
wr.writerow(['ParkID', 'SiteName', 'InspectionDate', 'OverallCondition', 'OverallCleanliness', 'Cleanliness/Glass'])

for entry in parkArray:
	wr.writerow(entry)

w.close()

