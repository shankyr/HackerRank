from collections import Counter

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arr_counter = Counter(arr)

for ind in xrange(100):
    try:
        print arr_counter[ind],
    except KeyError:
        print 0,
