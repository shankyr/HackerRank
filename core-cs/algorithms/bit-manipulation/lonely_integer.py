from collections import Counter

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
arr_counter = Counter(arr)

print [x for x in arr_counter.keys() if arr_counter[x] == 1][0]
