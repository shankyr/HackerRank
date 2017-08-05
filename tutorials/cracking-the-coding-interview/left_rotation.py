import timeit

start = timeit.default_timer()


def array_left_rotation(a, n, d):
    b = []
    for i in xrange(n):
        b.insert((i + n - d) % n, a[i])
    return b


n, d = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, d);
print ' '.join(map(str, answer))

print timeit.default_timer() - start
