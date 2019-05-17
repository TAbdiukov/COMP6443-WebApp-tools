import mechanize
import os
import re
import Queue
from BeautifulSoup import BeautifulSoup

def read_page(source, subs):
	for word in source.split():
		if word not in subs:
			subs[word] = 1
			with open("l1.txt", "a") as f:
				f.write(word)
				f.write("\n")

subs = {}
links = Queue.Queue()
links.put("http://kb.ns.agency")
done = ["http://kb.ns.agency"]
browser = mechanize.Browser()
while not links.empty():
	link = links.get()
	try:
		page = browser.open(link)
	except:
		continue
	source = page.read()
	read_page(source, subs)
	soup = BeautifulSoup(source)
	refs = soup.findAll(name = "a")
	for r in refs:
		if r.has_key("href"):
			print r["href"]
			if r not in done and "?" not in r["href"]:
				l = link + "/" + r["href"]
				print l
				done.append(l)
				links.put(l)
