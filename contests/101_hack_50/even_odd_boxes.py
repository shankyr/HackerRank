#https://www.hackerrank.com/contests/101hack50/challenges/even-and-odd-boxes
#!/bin/python3

import sys

def minimumChocolateMoves(n, X):
    # Complete this function
    count, count_1, count_2 = 0, 0, 0
    if ((n % 2 == 0 and (2 * sum(X)) < (3 * n)) or
        (n % 2 == 1 and (2 * sum(X)) < (3*n + 1)) or
        ((n % 4 == 0 or n % 4 == 1) and sum(X) % 2 == 1) or
        ((n % 4 == 2 or n % 4 == 3) and sum(X) % 2 == 0)):
        return -1
    else:
        for a0 in range(n):
            if (a0 % 2 != X[a0] % 2):
                if X[a0] == 1:
                    count_1 += 1
                else:
                    count_2 += 1
                count += 1
        if count_1 > count_2:
            return int (count/2 + (count_1 - count_2)/2)
        else:
            return int(count/2)

#  Return the minimum number of chocolates that need to be moved, or -1 if it's impossible.
q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    X = list(map(int, input().strip().split(' ')))
    result = minimumChocolateMoves(n, X)
    print(result)