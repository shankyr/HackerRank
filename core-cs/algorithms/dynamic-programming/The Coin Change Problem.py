#https://www.hackerrank.com/challenges/coin-change
#!/bin/python3

import sys

def getWays(n, c):
    len_c = len(c)
    #print (n, c)
    k = int(n/c[0])
    ways_count = 0
    if(len_c == 1):
        if (n % c[0] == 0):
            return 1
        else:
            return 0
    else:
        for a0 in range(k):
            #print (n - a0*c[0], c[1:])
            ways_count += getWays(n - a0*c[0], c[1:] ) 
        if (n % c[0] == 0):
            ways_count += 1
        else:
            ways_count += getWays(n - k*c[0], c[1:] )
    #print (n, c, ways_count)
    return ways_count
    # Complete this function

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
c.sort(reverse = True)
ways = getWays(n, c)
print (ways)