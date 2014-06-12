import csv

# Females over and under 18 by block
f = open("/Users/karaleary/nycep/output/censusOutput/ageOfFemales.csv")
lines = csv.reader(f, delimiter = ",")

blocks = {}

lines.next()

for line in lines:
	block = line[0]
	sumUnder18 = 0
	sumOver18 = 0
	for i in range(1,5):
		sumUnder18 += int(line[i])
	for i in range(6,len(line)):
		sumOver18 += int(line[i])
	blocks[block] = (sumUnder18, sumOver18)

f.close()

# Males over and under 18 by block
f = open("/Users/karaleary/nycep/output/censusOutput/ageOfMales.csv")
lines = csv.reader(f, delimiter = ",")

lines.next()

for line in lines:
	block = line[0]
	sumUnder18 = 0
	sumOver18 = 0
	for i in range(1,5):
		sumUnder18 += int(line[i])
	for i in range(6,len(line)):
		sumOver18 += int(line[i])
	blocks[block] += (sumUnder18, sumOver18)

f.close()

# Write results to output file
with open("/Users/karaleary/nycep/output/censusOutput/overUnder18.csv", "w") as w:
	writer = csv.writer(w, delimiter = ",")
	writer.writerow(["blockGroup", "under18", "over18"])
	for entry in blocks:
		totalUnder18 = blocks[entry][0] + blocks[entry][2]
		totalOver18 = blocks[entry][1] + blocks[entry][3]
		writer.writerow([entry, totalUnder18, totalOver18])
