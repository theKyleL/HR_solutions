# HackerRank
# Create a right-justified staircase with ‘spaces’ and ‘#’
# Input is an integer for the number of lines to print.
# Note: Last line is not preceeded with any spaces

import sys

n = int(input().strip())
spaces = ""
hashes = "#"

for i in range(n):
	spaces = ""
	for i in range(n-1-i):
		spaces += " "
		
	print(spaces + hashes)
	hashes += "#"
