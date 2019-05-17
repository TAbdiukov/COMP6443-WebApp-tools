import urllib2
import json

headers = {"Accept": "application/json", "Cookie": "zid=z5[redacted]3r1LBJo50PsJuGa_9ONl-d4dWKo"}
url = "http://drive.bing.ns.ag[redacted]"

for id in range(0, 300):
	u = url + str(id)
	req = urllib2.Request(u, None,  headers)
	try:
		resp = urllib2.urlopen(req)
	except urllib2.HTTPError as e:
		print str(id) + " - " + str(e.code)
	except Exception as e:
		print e
	else:
		#no exception
		data = resp.read()
		data = json.loads(data)
		print str(data["id"]) + " - " + data["author"] + " - " + data["name"] + " - " +  data["content"]
