import timeit

start = timeit.default_timer()


def merge_sort(alist):
    alist_length = len(alist)

    if alist_length <= 1:
        return alist

    else:
        split = alist_length / 2

        left = alist[:split]
        right = alist[split:]

        if len(left) > 1:
            left = merge_sort(left)

        if len(right) > 1:
            right = merge_sort(right)

        return merge(left, right)


def merge(l, r):
    global inversions

    l_length = len(l)
    r_length = len(r)
    i, j = 0, 0

    slist = []

    while i < l_length and j < r_length:

        if l[i] <= r[j]:
            slist.append(l[i])
            i += 1

        else:
            slist.append(r[j])
            j += 1

    if i < l_length:
        while i < l_length:
            slist.append(l[i])
            i += 1
    else:
        while j < r_length:
            slist.append(r[j])
            j += 1

    return slist


def pick_flavor(m, n, arr):
    sorted_arr = merge_sort(arr)

    for i in range(0, n):
        j = i + 1
        while j < n:
            if sorted_arr[i] + sorted_arr[j] == m:
                if sorted_arr[i] == sorted_arr[j]:
                    ch1 = arr.index(sorted_arr[i], 0) + 1
                    ch2 = arr.index(sorted_arr[j], ch1) + 1
                else:
                    ch1, ch2 = arr.index(sorted_arr[i]) + 1, arr.index(sorted_arr[j]) + 1
                print min(ch1, ch2), max(ch1, ch2)
                exit()

            elif sorted_arr[i] + sorted_arr[j] > m:
                break

            j += 1


t = int(raw_input().strip())
for test in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))

    pick_flavor(m, n, arr)

print timeit.default_timer() - start
