

n = int(raw_input().strip())
A = map(int, raw_input().strip().split(' '))

m = int(raw_input().strip())
B = map(int, raw_input().strip().split(' '))

A_set = set([])
A_counter = {}

for i in xrange(n):
    A_set.add(A[i])

    try:
        A_counter[A[i]] += 1
    except KeyError:
        A_counter[A[i]] = 1

B_set = set([])
B_counter = {}

ans = []

for i in xrange(m):
    try:
        B_counter[B[i]] += 1
    except KeyError:
        B_counter[B[i]] = 1

    if B[i] not in A_set or B_counter[B[i]] > A_counter[B[i]]:
        ans.append(B[i])

ans.sort()
prev = -1
for elem in ans:
    if elem != prev:
        prev = elem
        print elem,
