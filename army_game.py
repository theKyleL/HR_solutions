"""
Hackerrank problem: Army Game
Solution by: Kyle Latino

Problem:
Luke is daydreaming in math class. He has a sheet of graph paper with n rows and m columns, 
and he imagines that there is an army base in each cell for a total of n*m bases. He wants 
to drop supplies at strategic points on the sheet, marking each drop point with a red dot. 
If a base contains at least one package inside or on top of its border fence, then it's 
considered to be supplied. 

Given n and m, what's the minimum number of packages that Luke must drop to supply all of 
his bases?

"""


# imports


# globals
n, m = 0, 0


# functions
def readInputs():
	"""
	Read in the value pair as integer values
	"""
	global n, m
	n, m = list(map(int, input().split()))


def findMinimumDrops(n, m):
	"""
	Determine the number of edges on each row and column on the grid
	"""
	if n>1:
		n = n-1

	if m>1:
		m = m-1

	return n*m


# program
if __name__ == '__main__':
	readInputs()
	print(findMinimumDrops(n, m))
