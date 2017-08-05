# 28/28 tests passed
# https://www.hackerrank.com/contests/w34/challenges/maximum-gcd-and-sum
#!/bin/python3

import sys

def maximumGcdAndSum(A, B):
    # Complete this function
    max_A, max_B = max(A), max(B)
    maxi = max(max_A, max_B)
    ans = max_A + max_B
    set_A, set_B = set(A), set(B)
    #print (maxi)
    for i in range(maxi,1, -1):
        #print (i)
        count_A, count_B, tot_count = 0, 0, 0
        for j in range(int(maxi/i) * i, 0, -i):
            #print (j)
            if ((count_A == 0) and (j in set_A)):
                count_A += 1
                tot_count += 1
                max_A = j
            if ((count_B == 0) and (j in set_B)):
                count_B += 1
                tot_count += 1
                max_B = j
            if (tot_count == 2):
                ans = max_A + max_B
                break
        if (tot_count == 2):
            break
        #print (ans)
    
    return ans
        #print (maxi, set_A, set_B)

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    res = maximumGcdAndSum(A, B)
    print(res)