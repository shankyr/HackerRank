import timeit

start = timeit.default_timer()

n = int(raw_input().strip())

steps = list(raw_input().strip())

level = 0
valley = 0

for step in steps:
    if step == 'U':
        level += 1

        if level == 0:
            valley += 1
    else:
        level -= 1

print valley

print timeit.default_timer() - start
