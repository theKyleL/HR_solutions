#  Problem found on HackerRank
#  Solution by: Kyle Latino
#
#  Given a number of people, determine how many handshakes are necessary 
#  to ensure that everyone has shaken the hand of everyone else.


handshake_cache = {}

def getHandshakes(n):
	
	# look in the dictionary for the result before executing
	if n in handshake_cache:
		return handshake_cache[n]
	
	val = 0
	
	# compute number of handshakes
	if n == 1:
		# do nothing
		val = 0
	else:
		val = (getHandshakes(n-1) + (n-1))

	handshake_cache[n] = val
	return val

n = int(input("Enter number of test cases:"))
		
for _ in range(n):
	people = int(input("Enter number of people:"))
	print(getHandshakes(people))
	
