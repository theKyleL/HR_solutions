"""
Hackerrank problem: Minumum Height Tiangle
Solution by: Kyle Latino

Given integers b and a, find the smallest integer h, such that there exists a triangle of height h, base b, having an area of at least a.
"""


# imports
import math

# globals
a, b = 0, 0

# functions
def readInputs():
	global a, b
	b, a = list(map(int, input().split()))


def findH():
	""" known:
		area of triangle = (1/2) base * height
		thus: h = area / (1/2) base
		or: h = 2a / b
	"""
	h = (2*a) / b # calculate the precise value for h
	h = math.ceil(h) # round h up to the next integer value 
	return h


# program

if __name__ == '__main__':
	#read in values
	readInputs()
	print(findH())
