from collections import Counter


n = int(raw_input().strip())

s_arr = map(int, raw_input().strip().split(' '))

d, m = map(int, raw_input().strip().split(' '))

answer = 0

if m == 1:
    answer = Counter(s_arr)[d]
else:
    for i in xrange(n - m + 1):
        total = 0
        for j in xrange(m):
            total += s_arr[i + j]
            if total > d:
                break
        if total == d:
            answer += 1

print answer
