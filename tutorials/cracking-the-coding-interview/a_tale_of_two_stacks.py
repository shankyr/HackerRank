import timeit

start = timeit.default_timer()

queue = []
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.append(values[1])
    elif values[0] == 2:
        del queue[0]
    else:
        print queue[0]

print timeit.default_timer() - start

