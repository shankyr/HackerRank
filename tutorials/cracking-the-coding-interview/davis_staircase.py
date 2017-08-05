
import timeit

start = timeit.default_timer()


def possible_ways(n):
    global num_of_steps

    try:
        return num_of_steps[n]
    except IndexError:
        steps = possible_ways(n - 1) + possible_ways(n - 2) + possible_ways(n - 3)
        num_of_steps.append(steps)
        return steps


tests = int(raw_input().strip())

num_of_steps = [1, 1, 2, 4]
heights = []

for test in xrange(tests):
    height = int(raw_input().strip())
    heights.append(height)

possible_ways(max(heights))

for h in heights:
    print num_of_steps[h]

print timeit.default_timer() - start
