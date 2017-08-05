import timeit
from collections import Counter

start = timeit.default_timer()

n = int(raw_input().strip())

A = map(int, raw_input().strip().split(' '))

A_counter = Counter(A)

for k, v in A_counter.items():
    if v == 1:
        print k

print timeit.default_timer() - start
