import bisect
import timeit

start = timeit.default_timer()

n, m = map(int, raw_input().strip().split(' '))

A = {}
B = {}
for i in xrange(n):
    a, b = map(int, raw_input().strip().split(' '))

    try:
        A[a] += 1
    except KeyError:
        A[a] = 1

    try:
        B[b] += 1
    except KeyError:
        B[b] = 1


A_keys = sorted(A.keys(), reverse=True)
for i in xrange(1, len(A_keys)):
    A[A_keys[i]] += A[A_keys[i - 1]]


B_keys = sorted(B.keys())
for i in xrange(1, len(B_keys)):
    B[B_keys[i]] += B[B_keys[i - 1]]


A_keys = sorted(A.keys())
strength_sum = 0
for i in xrange(m):
    c, d = map(int, raw_input().strip().split(' '))

    ind = bisect.bisect_left(A_keys, d)
    if 0 <= ind < len(A_keys):
        if A_keys[ind] == d:
            ind += 1
        if 0 <= ind < len(A_keys):
            shots_a_greater_than_d = A[A_keys[ind]]
        else:
            shots_a_greater_than_d = 0
    else:
        shots_a_greater_than_d = 0

    ind = bisect.bisect_left(B_keys, c) - 1
    if 0 <= ind < len(B_keys) and B_keys[ind] < c:
        shots_b_less_than_c = B[B_keys[ind]]
    else:
        shots_b_less_than_c = 0

    strength_sum += n - (shots_a_greater_than_d + shots_b_less_than_c)

print strength_sum

print timeit.default_timer() - start
