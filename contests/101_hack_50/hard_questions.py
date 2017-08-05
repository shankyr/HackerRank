#https://www.hackerrank.com/contests/101hack50/challenges/hard-questions
#!/bin/python3

import sys

def maxScoreOfVincent(n, s, t):
    result = n
    for a0 in range(n):
        if (s[a0]==t[a0] or s[a0] == '.'):
            result -= 1
    return result
    # Complete this function

#  Return the maximum score of Vincent.
n = int(input().strip())
s = input().strip()
t = input().strip()
result = maxScoreOfVincent(n, s, t)
print(result)
