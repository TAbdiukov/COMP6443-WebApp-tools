#!/usr/bin/python  
import sys  
import time
import os
import requests
import re
import uuid

#import requests-futures
from baseconv import base62
from etaprogress.progress import ProgressBar


def main():
	PROGRAM_NAME = "intelBing"
	if len(sys.argv) != 2:
		print("USAGE: python "+PROGRAM_NAME+".py <attempts>")
		print("For example: python "+PROGRAM_NAME+".py 100")
	else:
		# init
		# https://stackoverflow.com/a/16060908
		
		attempts = int(sys.argv[1])
		
		logname = PROGRAM_NAME+"_"+str(int(time.time()))+".log"
		log = open(logname, "a+")
		
		cookies = {
			"zid": "z5214048",
			"token": "7f9beb00045ec2a7af0bbea5281c9e088025dc53fbf18fdefd8da90fb26d4684",
			"session": "eyJ1c2VybmFtZSI6IjM2QksxbUk0UnUifQ.D3fmSg.hMMOS2BM_bZ4P7wu0DtAjurIJoU"
		}
		
		URL_new = "http://pastebing.ns.agency/new"
		URL_pastes = "http://pastebing.ns.agency/pastes"
		raw_want_from = "<a href="+chr(34)+"/raw/"
		raw_want_to = chr(34)+" class="+chr(34)+"card-link"+chr(34)+">Raw paste</a>"
		
		work = attempts
		bar = ProgressBar(work, max_width=40)
		
		# print for user
		print(PROGRAM_NAME+" initialised")
		print("attempts: "+str(attempts))
		print("URL_new @ "+URL_new)
		print("URL_pastes @ "+URL_pastes)
		print("stdout will be logged to "+logname)
		print("the intel will start in 3s")
		# allow user to change mind
		time.sleep(3)
		
		#payload		
		for i in range(work):		
			# https://stackoverflow.com/a/17323913
			k=i+1
			k_string = str(k) # to save mem
			
			#enter input
			post = {
				"title": k_string+": "+genRandomString(),
				"contents": k_string+": "+genRandomString()
			}
			
			r = requests.post(URL_new, cookies=cookies, data=post)
			
			#log.write(r.text)
			#print("1 "+str(len(r.text)))
			#os.system("pause")
			
			#get output
			r = requests.get(URL_pastes, cookies=cookies)
			soup = r.text
			
			#log.write(r.text)
			#print("2 "+str(len(r.text)))
			#os.system("pause")
			
			#process
			raw_link = find_between(soup, raw_want_from, raw_want_to)
			
			# to log + print
			
			whatToLog = "[L] "+raw_link
				
			log.write(whatToLog+"\n")
			print(k_string+" "+whatToLog)
			
			bar.numerator = i
			print(str(bar))
			#sys.stdout.flush()
			
			#time.sleep(SLEEP_TIME/1000)
		
		#payload (for-loop) over
		whatToLog = "Fin"
				
		log.write(whatToLog+"\n")
		print(raw_link+" "+whatToLog)
		
		log.close()

# https://stackoverflow.com/a/17323913
def genRandomString():
	return str(uuid.uuid4())

def toHexCustom(dec): 
	return str(hex(dec).split('x')[-1])	
	
# https://stackoverflow.com/a/3368991
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""
	
if __name__ == '__main__':
	main()