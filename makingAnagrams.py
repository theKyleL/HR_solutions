"""
HackerRank Example problem Arrays: Strings: Making Anagrams
Solution by: Kyle Latino

Problem: 
	Given two strings, a and B, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings. 
	
Input Format
The first line contains a single string, a. 
The second line contains a single string, b.

Constraints

It is guaranteed that a and b consist of lowercase English alphabetic letters (i.e., a through z).

Output Format
Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

Sample Input
cde
abc

Sample Output
4

Explanation
We delete the following characters from our two strings to turn them into anagrams of each other:
Remove d and e from cde to get c.
Remove a and b from abc to get c.
We must delete  characters to make both strings anagrams, so we print  on a new line
"""

# from collections import  


def number_needed(a, b):
	
	#convert strings to lists
	aList = list(a)
	bList = list(b)
	matchList = list()
	
	# identify chars that are present in both lists
	for i in aList:
		if i in bList:
			matchList.append(i)
			# remove chars to prevent duplication
			bList.remove(i)

	# return the number of chars that must be removed to create identical lists	
	return (len(a) + len(b)) - (2 * len(matchList))


a = list(input().strip())
b = list(input().strip())


print(number_needed(a, b))
