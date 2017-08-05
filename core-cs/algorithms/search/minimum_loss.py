
n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
arr_order = {}
for i in xrange(n):
    arr_order[arr[i]] = i

arr_sorted = sorted(arr)

min_loss = 10 ** 16
for i in xrange(1, n):
    selection_loss = arr_sorted[i] - arr_sorted[i - 1]
    if selection_loss < min_loss and arr_order[arr_sorted[i]] < arr_order[arr_sorted[i - 1]]:
        min_loss = selection_loss

print min_loss
