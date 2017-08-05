#!/bin/python

N = int(raw_input().strip())
B = map(int, raw_input().strip().split(' '))

ans = 0

for ind in xrange(len(B) - 1):
    if B[ind] % 2 != 0:
        B[ind] += 1
        B[ind + 1] += 1
        ans += 2

if sum(B) % 2 == 0:
    print ans
else:
    print "NO"
