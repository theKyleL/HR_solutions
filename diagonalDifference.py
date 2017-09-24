# Hackerrank problem Conecting Towns
# 

# get number of test cases
t = int(input())

# calculate number of possible routes
def findNumRoutes():
    numTowns = int(input())
    
    routes = list(map(int, input().split()))  # store values as a list of integers 
    
    totalRoutes = routes[0]
    # find an efficient method for calculating the product of all integers
    for i in routes:
        totalRoutes *= i
    
    print(totalRoutes)
    
    
for _ in range(t):
    findNumRoutes()