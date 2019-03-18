#!/usr/bin/python  
import sys  
import socket, struct
import zlib
import time
import os
import requests

def main():
	if len(sys.argv) != 2:
		print("USAGE: python bruteGetIPs.py (URL)")
		print("For example: python bruteGetIPs.py http://dns.sso.ns.agency/api/lookup?ip=")
	else:
		# init
		PROGRAM_NAME = "bruteGetIPs"
		URL = str(sys.argv[1])
		SLEEP_TIME = 1/1000
		
		logname = PROGRAM_NAME+"_"+str(int(time.time()))+".log"
		log = open(logname, "a+")
		
		ip_min = 0
		ip_max = (2**32)-1
		# print for user
		print(PROGRAM_NAME+" initialised")
		print("URL: "+URL)
		print("stdout will be logged to "+logname)
		print("the bruteforce will start in 3s")
		# allow user to change mind
		time.sleep(3)
		
		#payload
		for i in range(ip_max-ip_min+1):
			k=i+ip_min
			k_string = int2ip(k) # the trivial IP address
			r = requests.get(URL+k_string)
			txt = r.text
			# https://docs.python.org/3/library/zlib.html SAYS
			#'An Adler-32 checksum is almost as reliable as a CRC32 but can be computed much more quickly'
			#'Changed in version 3.0: Always returns an unsigned value' => GOOD
			txt_hash = toHexCustom(zlib.adler32(txt.encode('utf-8')))
			
			# write to IPs listings
			f_ips = open("ips_"+txt_hash+".txt", "a+")
			f_ips.write(k_string+"\n")
			f_ips.close()
			
			# if no transcription => first time resp encountered
			if not(os.path.isfile("plain_"+txt_hash+".txt")):
				# write to plaintext transcription
				f_plain = open("plain_"+txt_hash+".txt", "w+")
				f_plain.write(txt)
				f_plain.close()
				# now log stuff
				whatToLog = "[N]"+k_string+"; New hash found! Check file: "+"plain_"+txt_hash+".txt"
				
				log.write(whatToLog+"\n")
				print(whatToLog)
			
			# if hash already encountered
			else:
				# boring log, what else to do
				whatToLog = "[B]"+k_string+": "+txt_hash+" ("+str(r.status_code)+")"
				
				log.write(whatToLog+"\n")
				#print(whatToLog)
				
			#time.sleep(SLEEP_TIME/1000)
		
		#payload (for-loop) over
		whatToLog = "[F] Fin"
				
		log.write(whatToLog+"\n")
		print(whatToLog)
		
		log.close()
				
# https://stackoverflow.com/a/19452910
def int2ip(ip):
	return socket.inet_ntoa(struct.pack('!L', ip))
	
def toHexCustom(dec): 
	return str(hex(dec).split('x')[-1])
	
if __name__ == '__main__':
	main()