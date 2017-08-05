import timeit

start = timeit.default_timer()

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arr_sorted = sorted(arr)

unsorted_indices = []
for ind in xrange(n):
    if arr[ind] != arr_sorted[ind]:
        unsorted_indices.append(ind)

if len(unsorted_indices) == 2:
    print "yes"
    print "swap", unsorted_indices[0] + 1, unsorted_indices[1] + 1

else:
    arr_subset = arr[unsorted_indices[0]:unsorted_indices[-1] + 1]
    arr_sub_set_reverse_sorted = sorted(arr_subset, reverse=True)
    if arr_subset == arr_sub_set_reverse_sorted:
        print "yes"
        print "reverse", unsorted_indices[0] + 1, unsorted_indices[-1] + 1
    else:
        print "no"

print timeit.default_timer() - start
