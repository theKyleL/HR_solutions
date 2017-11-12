"""
Hackerrank problem "Grading Students"
Solution by Kyle Latino

HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from 0 to 100.
Any  less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
For example, 84 will be rounded to 85 but 29 will not be rounded because the rounding would result in a number that is less than 40.

Given the initial value of grade for each of Sam's n students, write code to automate the rounding process. For each grade, round it according to the rules above and print the result on a new line.

"""
__author__ = 'Kyle Latino'

#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        if grades[i] > 37:
            roundDiff = grades[i]%5
#            print(roundDiff)
            if roundDiff > 2:
                grades[i] += (5-roundDiff)
#        print(grades[i])
    return grades

if __name__ == "__main__":
    n = int(input().strip())
    grades = []
    grades_i = 0
    for grades_i in range(n):
        grades_t = int(input().strip())
        grades.append(grades_t)
    result = solve(grades)
    print ("\n".join(map(str, result)))
