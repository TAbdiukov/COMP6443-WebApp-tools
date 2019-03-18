import sys
import string
import pyperclip
import math
from etaprogress.progress import ProgressBar

def PROGRAM_NAME(): return "gent"

def doHelp():
	print("gent - Generate Table")
	print("(and copy to clipboard)")

	print("USAGE:")
	print("python "+PROGRAM_NAME() +".py [for default output of ASCII 32-255, OR:]")
	print("python "+PROGRAM_NAME() +".py <min> <max> [for values from <min> to <max> incl.]")
	print("")
	print("For example: python "+PROGRAM_NAME()+".py 1 65535")
	print("")

def main():
	argc = len(sys.argv) - 1
	if (argc == 0): # default
		doHelp()
		min = 32
		max = 255
	elif (argc == 2): #user defined
		min = int(sys.argv[1])
		max = int(sys.argv[2])
	else:
		doHelp()
		sys.exit(0)
	
	# error-fixing
	if(min<0):min=1
	if(max<0):max=1
	if(min>=0x110000):min=0x110000-1
	if(max>=0x110000):max=0x110000-1
	
	work = max-min
	work_minestone = math.ceil(work / 5) # ceil = floor up
	bar = ProgressBar(work, max_width=50)
	
	i = 0
	s = ""
	
	for i in range(work+1):
		k = i + min
		c = chr(k)
		s = s+c

		if (k % work_minestone) == 0:
			bar.numerator = i
			print(bar)
			sys.stdout.flush()
		
	bar.numerator = i
	print(bar)
	print("")
	
	pyperclip.copy(s)
	print("done")
	
if __name__ == '__main__':
	main()