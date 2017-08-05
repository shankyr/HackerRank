from collections import Counter

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arr_counter = Counter(arr)

for ind in xrange(100):
    try:
        for i in xrange(arr_counter[ind]):
            print ind,
    except KeyError:
        pass
