
tests = int(raw_input().strip())

for t in xrange(tests):

    elem_found = False

    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))

    if len(arr) in (0, 1):
        print "YES"
        continue
    elif len(arr) == 2:
        if arr[0] == arr[1]:
            print "YES"
        else:
            print "NO"
        continue

    left_sum, right_sum = 0, sum(arr) - arr[0]
    for i in xrange(1, n - 1):
        # print i, arr[:i], arr[i + 1:]
        left_sum += arr[i - 1]
        right_sum -= arr[i]
        if left_sum == right_sum:
            elem_found = True
            break

    if elem_found:
        print "YES"
    else:
        print "NO"
