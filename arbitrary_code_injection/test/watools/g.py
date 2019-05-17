import urllib

with open("bl.txt", "r") as f:
	for line in f.readlines():
		string = "http://pastebing.ns.agency/raw/2uKX"
		string += line
		page = urllib.urlopen(string)
#		try:
#			page = urllib.request.urlopen(string)
#		except:
#			pass
		if len(page.read()):
			with open("r1.txt", "w") as g:
				g.write(page.read() + "\n")
		page.close()
