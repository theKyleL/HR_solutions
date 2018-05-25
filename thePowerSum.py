"""
Hackerrank problem: The Power Sum (attempt to utilize recursion)
Solution by: Kyle Latino

Problem:
Find the number of ways that a given integer, X, can be expressed as 
the sum of the Nth powers of unique, natural numbers. 

For example, if X = 13 and N = 2, we have to find all compinations of 
unique squares adding up to 13. The only solution is 2^2 + 3^2. 

IN:

10
2

OUT:

1


Model:

read in values for x and n


"""


# imports
import math

# globals


# functions

# def outputStatus(text):
# 	print(text)


def readInputNumber():
	"""
	Read in an integer value and return it.
	"""
	return int(input())


def powerSum(X, N):
	# Complete this function
	totalSolutions = 0
	for i in range(X, 0, -1):
		print('running for ', i)
		sum = 0
		for j in range(i, 0, -1):
			print('begining while loop for ', j)
			if ((sum + math.pow(j,N))):
				print('adding to sum')
				sum += math.pow(j,N)
				if sum == X:
					totalSolutions += 1
	return totalSolutions


# program
if __name__ == '__main__':
	X = readInputNumber()
	N = readInputNumber()
	result = powerSum(X, N)
	print(result)
