import timeit

start = timeit.default_timer()

print len([x for x in list(raw_input().strip()) if x.isupper()]) + 1

print timeit.default_timer() - start
