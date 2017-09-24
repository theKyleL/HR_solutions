arr = 0
e = 0
sorted = False


def initialize():
	global arr, e, sorted
	e = int(input()) - 1  # location of the inserted element
	arr = list(map(int, input().strip().split()))


def sort():
	global arr, e, sorted
	if arr[e] < arr[e-1]:
		swapSpots()
	else:
		sorted = True


def swapSpots():
	global arr, e, sorted
	temp = arr[e]
	arr[e] = arr[e-1]
	printList()
	arr[e-1] = temp
	e = e-1


def printList():
	global arr
	print(' '.join(str(val) for val in arr))


initialize()

while not sorted and e > 0:
	sort()

printList()