# HackerRank
# Given an array of integers, calculate which fraction 
# of the elements are positive, negative, and zero, 
# respectively. Print the decimal value of each fraction 
# on a new line.

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split('')]
gtz = 0
ltz = 0
ez = 0

# bin the results
for i in range(n):
	if arr[i] > 0:
		gtz += 1
	elif arr[i] < 0:
		ltz += 1
	else:
		ez += 1
		
# solve for fractions
gtz /= n
ltz /= n
ez /= n

print(str(gtz) + '\n' + str(ltz) + '\n' + str(ez))
