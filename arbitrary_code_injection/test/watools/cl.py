import re
with open("l3.txt", "r") as f:
	pat = re.compile("[^a-z0-9-]")
	for line in f.readlines():
		line = line.strip()
		line = line.lower()
		line = line.split(".")
		line = "".join(line)
		if pat.search(line) is not None:
			continue
		print line
