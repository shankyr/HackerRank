import timeit

start = timeit.default_timer()


def count_swaps(length, org):

    org_dict = {}

    for i in xrange(length):
        org_dict[org[i]] = i

    srt = sorted(org)

    swaps = 0
    for ind in xrange(length):
        if srt[ind] != org[ind]:
            swap_index = org_dict[srt[ind]]
            org_dict[org[ind]] = swap_index
            org[ind], org[swap_index] = srt[ind], org[ind]

            swaps += 1

    return swaps


# input array of integers that need to be sorted
n = int(raw_input().strip())

inp = map(int, raw_input().strip().split(' '))
reverse_inp = list(reversed(inp))

print min(count_swaps(n, inp), count_swaps(n, reverse_inp))

print timeit.default_timer() - start
