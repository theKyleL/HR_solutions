

import sys
import re

def timeConversion(s):
	# code here
	time = list(map(str, s.strip().split(":")))
	#print(time)
	convertTime = time[2]
	
	if "PM" in convertTime:
		time[0] = str(int(time[0]) + 12)
		return(time[0] + ":" + time[1] + ":" + time[2]).replace("PM", "")
	else:
		return(time[0] + ":" + time[1] + ":" + time[2]).replace("AM", "")
		
s = input().strip()
result = timeConversion(s)
print(result)

