zcta = []

with open("../output/zbp/zcta.txt") as f:
	for line in f:
		zcta.append(int(line))

i = 0

w = open("../output/zbp/zbp12detailCleaned.txt", "wb")

with open("../data/zbp/zbp12detail.txt") as f:
	for line in f:
		if (i == 0):
			i += 1
			w.write(line)
			continue
		newline = line.split("\"")
		zc = newline[1]
		if int(zc) in zcta:
			w.write(line)

w.close()