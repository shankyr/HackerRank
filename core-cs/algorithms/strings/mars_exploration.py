import timeit

start = timeit.default_timer()

s = list(raw_input().strip())

correct_string = ['S', 'O', 'S']
changes = 0

for ind in xrange(len(s)):
    if s[ind] != correct_string[ind % 3]:
        changes += 1

print changes

print timeit.default_timer() - start
