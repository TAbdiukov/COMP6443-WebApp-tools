with open("l4.txt", "r") as f:
	words = {}
	for line in f.readlines():
		line = line.strip()
		for word in line.split("-"):
			words[word] = 1
for line in words:
	print line
