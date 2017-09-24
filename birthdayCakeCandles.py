# HackerRank
# find the the count of the max value in an array
# 

import sys

def birthdayCakeCandles(n, ar):
	reachableCandles = 0
	maxHeight = max(ar)
	for i in range(n):
		if ar[i] == maxHeight:
			reachableCandles += 1
	
	return reachableCandles
	
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result [ birthdayCakeCandles(n, ar)]
print(result)
