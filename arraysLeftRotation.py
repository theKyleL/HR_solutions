"""
HackerRank Example problem Arrays: Left rotation
Solution by: Kyle Latino

Problem: 
	Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers
"""

def array_left_rotation(a, n, k):
    b = a[k:] # copy the tail of the initial list into the empty list
    for i in range(k):
        b.append(a[i]) # append the remaining items to the list.
    return b # return the list


# the following two lines are commented out for testing with fixed input
#n, k = map(int, input().strip().split(' '))
#a = list(map(int, input().strip().split(' ')))
a = [1, 2, 3, 4, 5]
n = 5
k = 2
answer = array_left_rotation(a , n, k);
print(*answer, sep=' ')
