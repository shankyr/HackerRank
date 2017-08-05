# 7/7 tests passed
# https://www.hackerrank.com/contests/w34/challenges/once-in-a-tram


#!/bin/python3

import sys

def onceInATram(x):
    # Complete this function
    last_3_digits, first_3_digits  = 0, 1
    while (last_3_digits != first_3_digits):
        x += 1
        z, last_3_digits, first_3_digits  = x, 0, 0
        for i in range (1,4):
            last_3_digits += z % 10
            z = int(z/10)
        for i in range (1,4):        
            first_3_digits += z % 10
            z = int(z/10)
    return (x)
            
if __name__ == "__main__":
    x = int(input().strip())
    result = onceInATram(x)
    print(result)
