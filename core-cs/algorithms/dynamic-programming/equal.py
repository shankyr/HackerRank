#!/bin/python3

import sys

def getWays(n, c, index):
    if (n == 0):
        return 1
    if (index >= len(c)):
        return 0
    amountWithCoin = 0
    ways = 0
    #print(index)
    while (amountWithCoin <= n):
        remaining = n - amountWithCoin
        #print(n, remaining, c, index + 1 , ways)
        ways += getWays(remaining, c, index + 1)
        #print(n, remaining, c, index , ways)
        amountWithCoin += c[index]
    return ways
    # Complete this function

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
#c.sort(reverse = True)
ways = getWays(n, c, 0)
print (ways)
