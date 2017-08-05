from collections import Counter

n = int(raw_input().strip())
arr = []
for i in xrange(n):
    arr.append(int(raw_input().strip().split(' ')[0]))

arr_counter = Counter(arr)

prev = 0
for ind in xrange(100):
    try:
        curr = arr_counter[ind]
        print prev + curr,
        prev += curr
    except KeyError:
        curr = 0
        print prev + curr,
        prev += curr
