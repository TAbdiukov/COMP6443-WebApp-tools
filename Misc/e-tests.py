#!/usr/bin/python  
import sys  
import math

def main():
	if len(sys.argv) != 1:
		print("USAGE: python experiment_NatureChange.py (raw measume)")
		print("For example: python experiment_NatureChange.py 3600 [for 1 hour]")
	else:
		#CONSTANTS
		PROGRAM_NAME = "experiment_NatureChange"
		
		EULER = math.e # or math.exp(1)
		GOLDEN = (1 + 5 ** 0.5) / 2 #ez
		PI = math.pi
		
		

if __name__ == '__main__':
	main()