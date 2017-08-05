#!/bin/python3

import sys

def patternCount(s):
    seq, count = '0', 0
    for i, value in enumerate(s):
        if value == '1':
            if seq == '10':
                count+=1 
            seq = '1'
        elif value == '0':
            if (seq == '1' or seq == '10'):
                seq = '10'
            else:
                seq = '0'
        else:
            seq = '0'
        # print (value + " " + seq)
    return count
    # Complete this function

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)
