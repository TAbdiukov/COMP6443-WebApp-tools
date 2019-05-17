with open("c2.txt", "r") as f:
	subs = []
	for l in f.readlines():
		s = l.split(".")
		n = len(s)
		s = s[0:n - 2]
		l = ".".join(s)
		subs.append(l)
for d in subs:
	print d
