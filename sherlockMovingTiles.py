""" hackerrank problem "Sherlock and Moving Tiles"
Solution by: Kyle Latino

Sherlock is given 2 square tiles, initially both of whose sides have length L placed in an  plane; 
so that the bottom left corner of each square coincides with the the origin and their sides are parallel to the axes.

At t=0, both squares start moving along the line x=y (along the positive x and y) with velocities S1 and S2.

For each query of form qi, Sherlock has to report the time at which the overlapping area of tiles is equal to qi.
"""
 

# Find the time where qL**2 == qi     
def solveForTime(area, s1, s2, L):
    """
    Input: desired area, speed1, speed2, Length_of_sides
    Output: time
    """
    return (sqrt(2*area**2)/abs(s1-s2))


# read in the length L, speed1, and speed2
input1 = list(map(int, input().split()))

# read in the number of test cases
testCases = int(input())
for i in range(testCases):
	print(solveForTime(int(input()), input1[0], input1[1], input1[2]))
