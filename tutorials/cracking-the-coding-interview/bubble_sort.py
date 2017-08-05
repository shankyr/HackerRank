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

    left_elements_added = 0

    slist = []

    while i < l_length and j < r_length:

        if l[i] <= r[j]:
            slist.append(l[i])
            i += 1

            left_elements_added += 1

        else:
            slist.append(r[j])
            j += 1

            inversions += l_length - left_elements_added

    if i < l_length:
        while i < l_length:
            slist.append(l[i])
            i += 1
    else:
        while j < r_length:
            slist.append(r[j])
            j += 1

    return slist

inversions = 0

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

sorted_a = merge_sort(a)

print "Array is sorted in", inversions, "swaps."
print "First Element:", sorted_a[0]
print "Last Element:", sorted_a[-1]

print timeit.default_timer() - start
