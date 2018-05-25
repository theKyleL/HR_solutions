"""

Hackerrank problem: nCr Table
Solution by: Kyle Latino

Jim is doing his discrete maths homework which requires him to
repeatedly calculate nCr(n choose r) for different values of n.
Knowing that this is time consuming, he goes to his sister June for
help. June, being a computer science student knows how to convert
this into a computer program and generate the answers quickly. She
tells him, by storing the lower values of nCr(n choose r), one can
calculate the higher values using a very simple formula.

If you are June, how will you calculate nCr values for different values of n?
Since values will be large you have to calculate them modulo 10^9.
"""

#!/bin/python3

import os
import sys


# Complete the solve function below.
def solve(n):
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print(fptr)

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

