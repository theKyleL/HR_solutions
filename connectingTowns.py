# Hackerrank problem Conecting Towns


# calculate number of possible routes
def findNumRoutes():
    numTowns = int(input())
    routes = list(map(int, input().split()))  # store values as a list of integers 
    totalRoutes = routes[0]
    # find an efficient method for calculating the product of all integers
    for i in range(1, len(routes)):
        totalRoutes *= routes[i]
    
    print(totalRoutes)

# get number of test cases
t = int(input())

for _ in range(t):
    findNumRoutes()
    