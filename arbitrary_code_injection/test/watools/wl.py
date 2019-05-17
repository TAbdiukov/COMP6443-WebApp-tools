subs = {}
with open("o1.txt", "r") as f:
	for l in f.readlines():
		a = False
		i = l.find("..")
		if i != -1:
			s = l.split("..")
			l = ".".join(s)
			a = True
		if "." == l[-1]:
			l = l[:-1]
			a = True
		if a:
			subs[l] = 1
subs2 = {}
with open("subdomains-10000.txt", "r") as f:
	for l in f.readlines():
		subs2[l] = 1
with open("deepmagic.com-top50kprefixes.txt", "r") as f:
	for l in f.readlines():
		if l not in subs2:
			subs[l] = 1
with open("n1.txt", "w") as f:
	for l in subs:
		f.write(l)
