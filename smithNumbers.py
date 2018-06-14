#!/bin/python3

'''
A Smith number is a composite number, the sum of whose digits is the 
sum of the digits of its prime factors obtained as a result of prime 
factorization (excluding ). The first few such numbers are 4, 22, 27, 
58, 85, 94, and 121.

Print '1' to Stdout if the number is a smith number else, print '0'.
'''

import os
import sys

# Complete the solve function below.
def solve(n):
	# calculate the sum of the digits
	sumD = calcSumOfDigits(n)


	# calculate the sum of the prime factors
	sumF = calcSumFactors(n)


	# compare the two sums
	if sumD == sumF:
		return 1
	else:
		return 0


# calculate and return the sum of the digits
def calcSumOfDigits(n):
	pass


# calculate and return the sum of the prime factors
def calcSumFactors(n):
	pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()

