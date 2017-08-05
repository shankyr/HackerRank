import timeit

start = timeit.default_timer()


def calc_min_diff(n, inp):
    minimum = 2 * (10 ** 9)

    for i in xrange(n - 1):
        curr_min = abs(inp[i] - inp[i + 1])
        if curr_min < minimum:
            minimum = curr_min

    return minimum


n = int(raw_input().strip())
inp = map(int, raw_input().strip().split(' '))

inp.sort()

print calc_min_diff(n, inp)

print timeit.default_timer() - start
