# Problem found on hackerrank.com
# Quicksort 1 - Partition
# 
'''
you can save yourself some trouble by utilizing python’s sort method on lists

# read in the first line
n = int(input())

# read in the array as a list
inputArray = list(map(int, input().split()))

# sort the list
inputArray.sort()

# print the sorted list separated by spaces
print(*inputArray)

because this feels like cheating, I've included a more 'proper' solution
'''

# imports

# global variables
__author__ = 'Kyle Latino'
left = []
equal = []
right = []

# function definitions
def addLeft(n):
	left.append(n)


def addRight(n):
	right.append(n)
	
	
def addEqual(n):
	equal.append(n)
	

# program execution
if __name__ == '__main__':
	n = int(input()) # read in length of input arr
	inArray = list(map(int, input().split()))
	pivot = inArray[0]
	for i in range(n):
		if inArray[i] < pivot:
			addLeft(inArray[i])
		elif inArray[i] == pivot:
			addEqual(inArray[i])
		else:
			addRight(inArray[i])
		
	print(*left, *equal, *right)