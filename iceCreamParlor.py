# read data for test case and output 
def choose():
    money = int(input())
    numFlavors = int(input())
    flavList = list(map(int, input().split()))
    # find flavors that spend all money
    for i in range(numFlavors - 1):
        for j in range(i+1, numFlavors):
            if flavList[i] + flavList[j] == money:
                print(int(i+1), int(j+1))
                return
    

# determine number of cases
n = int(input())


# iterate over each case
for i in range(n):
    # select flavors
    choose()