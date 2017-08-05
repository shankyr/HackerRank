# all tests passed

import heapq


n = int(raw_input().strip())
ar1 = map(int, raw_input().strip().split(' '))
ar2 = map(int, raw_input().strip().split(' '))

arr1_heap = []
arr2_heap = []

for i in xrange(len(ar1)):
    heapq.heappush(arr1_heap, (ar1[i], i))

for i in xrange(len(ar2)):
    heapq.heappush(arr2_heap, (ar2[i], i))


arr1_val1, arr1_ind1 = heapq.heappop(arr1_heap)
arr2_val1, arr2_ind1 = heapq.heappop(arr2_heap)

if arr1_ind1 != arr2_ind1:
    min_sum = arr1_val1 + arr1_val1
else:
    arr1_val2, arr1_ind2 = heapq.heappop(arr1_heap)
    arr2_val2, arr2_ind2 = heapq.heappop(arr2_heap)

    min_sum = min(arr1_val1 + arr2_val2, arr1_val2 + arr2_val1)

print min_sum
