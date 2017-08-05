import timeit

start = timeit.default_timer()

n = int(raw_input().strip())
candles = map(int, raw_input().strip().split(' '))

tallest = max(candles)

print candles.count(tallest)

print timeit.default_timer() - start
