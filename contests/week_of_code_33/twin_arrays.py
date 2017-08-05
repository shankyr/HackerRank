#!/bin/python3

# https://www.hackerrank.com/contests/w33/challenges/twin-arrays/problem
# Challenge: You are given two arrays A and B each containing n integers. You need to choose exactly one number 
# from A and exactly one number from B such that the index of the two chosen numbers is not same and 
# the sum of the 2 chosen values is minimum.

# Your objective is to find and print this minimum value.
# For example in the image shown below 1 + 6 or 2 + 5 is the minimum sum and not 1 + 5
# Array A : [3, 1, 4, 2], Array B: [6, 5, 8, 9]

# Input Format
# The first line contains an integer n denoting the size of two arrays. 
# Each of the next two lines contains n space separated integers denoting array A and B respectively.

# Constraints: 2<= n <= 10^5, 1<= array elements <= 10^5

# Output Format
# Print the minimum sum which can be obtained under the conditions mentioned in the problem statement.

import sys

def twinArrays(ar1, ar2):
    # Collect min in array1 and its loc
    ar1_min1, ar1_min1_loc = min(ar1), ar1.index(min(ar1))
    # Collect 2nd min in array1 and its loc
    ar1[ar1_min1_loc] = max(ar1) + 1
    ar1_min2, ar1_min2_loc = min(ar1), ar1.index(min(ar1))
    
    # Collect min in array1 and its loc
    ar2_min1, ar2_min1_loc = min(ar2), ar2.index(min(ar2))
    # Collect 2nd min in array1 and its loc
    ar2[ar2_min1_loc] = max(ar2) + 1
    ar2_min2, ar2_min2_loc = min(ar2), ar2.index(min(ar2))
    
    # check if array1_min loc is same as array2_min loc
    if (ar1_min1_loc == ar2_min1_loc):
        return min(ar1_min1 + ar2_min2, ar1_min2 + ar2_min1)
    else :
        return ar1_min1 + ar2_min1


n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)
