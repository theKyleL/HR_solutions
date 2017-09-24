# HackerRank
# Given five positive integers, find the maximum and 
# minimum values that can be calculated by summing exactly 
# four of the five integers. Then print the respective 
# minimum and maxumum values as a single line of two space 
# separated long integers.  
# 
# Print the min and max values on one line separated by a space. 

import sys

arr = list(map(int, input().strip().split(' ')))
# print(arr)
arr = sorted(arr)
# print(arr)
maxSum = sum(arr) - min(arr)
minSum = sum(arr) - max(arr)

print(str(minSum) + " " + str(maxSum))

