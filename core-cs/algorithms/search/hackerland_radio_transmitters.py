#https://www.hackerrank.com/challenges/hackerland-radio-transmitters

#!/bin/python3

import sys
from collections import deque

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]

#to remove duplicates and sort
x= list(set(x))
x.sort()

# setting initial parameters
count = 1
a0 = x[0]
coverage_end = a0 + 2*k
tower_postn = a0 + k

# sequentially check for tower position and coverage-end 
for i in x:
    if i > tower_postn:
        coverage_end = a0 + k 
        tower_postn = a0 + 2*k + 1
        
    if i > coverage_end:
        coverage_end = i + 2*k
        tower_postn = i + k
        count += 1
        
    a0 = i
print (count)