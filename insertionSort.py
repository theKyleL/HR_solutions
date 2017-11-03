"""
Hackerrank problem "Insertion sort"
Solution by Kyle Latino
"""
__author__ = 'Kyle Latino'


# global variables
arr = 0
e = 0
sorted = False


def initialize():
	"""
	Set all variables from STDIN
	"""
	global arr, e, sorted
	e = int(input()) - 1  # location of the inserted element
	arr = list(map(int, input().strip().split()))


def sort():
	"""
	Check order and handle sorting
	"""
	global arr, e, sorted
	if arr[e] < arr[e-1]:
		swapSpots()
	else:
		sorted = True


def swapSpots():
	"""
	Perform variable swap
	"""
	global arr, e
	temp = arr[e]
	arr[e] = arr[e-1]
	printList()
	arr[e-1] = temp
	e = e-1


def printList():
	"""
	Print the value of 'arr' to STDOUT.
	"""
	global arr
	print(' '.join(str(val) for val in arr))


if __name__ == '__main__':
	initialize()

	while not sorted and e > 0:
		sort()

	printList()
