#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HackerRank
# Create a right-justified staircase with ‘spaces’ and ‘#’
# Input is an integer for the number of lines to print.
# Note: Last line is not preceeded with any spaces


n = int(input())
if type(n) is int:
	spaces = ""
	hashes = "#"

	for i in range(n):
		spaces = ""
		for i in range(n-1-i):
			spaces += " "
		
		print(spaces + hashes)
		hashes += "#"
