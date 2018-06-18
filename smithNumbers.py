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
	sum = 0
	number = n
	while number > 0:
		sum += number % 10  # add the digit in the 1's place to the sum
		number = number // 10  # truncate the digit in the 1's place
	return sum


# calculate and return the sum of the prime factors
def calcSumFactors(n):
	sum = 0

	# make a list of factors
	factors = findPrimeFactors(n)
	for x in factors:
		sum += calcSumOfDigits(x)
	return sum


def findPrimeFactors(n):
	primeList = getPrimeList((n+1)//2)
	primeFactors = list()
	temp = n

	#  determine prime factors of value 'n'
	for i in primeList:
		while temp % i == 0:
			primeFactors.append(i)
			temp = temp / i
	return primeFactors


# Sieve of Eratosthenes 
# implementation by Srikar Appalaraju on StackOverflow.com
def getPrimeList(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = solve(n)
    fptr.write(str(result) + '\n')
    fptr.close()
