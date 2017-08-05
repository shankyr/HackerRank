import timeit
import bisect

start = timeit.default_timer()


def read_input():
    nLocal1, kLocal1 = map(int, raw_input().strip().split(' '))
    ALocal1 = map(int, raw_input().strip().split(' '))
    BLocal1 = map(int, raw_input().strip().split(' '))

    return nLocal1, kLocal1, ALocal1, BLocal1


def check_perm_exists(nLocal2, kLocal2, ALocal2, BLocal2):
    BLocal2.sort()

    for i in xrange(nLocal2):
        search_for = kLocal2 - ALocal2[i]
        index = bisect.bisect_left(BLocal2, search_for)

        if 0 <= index < len(BLocal2):
            del BLocal2[index]

        else:
            return "NO"

    return "YES"


qrs = int(raw_input().strip())

for q in xrange(qrs):
    n, k, A, B = read_input()
    print check_perm_exists(n, k, A, B)

print timeit.default_timer() - start
