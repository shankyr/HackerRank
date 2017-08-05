from collections import Counter
import timeit

start = timeit.default_timer()

tests = int(raw_input().strip())

for t in xrange(tests):
    w = list(raw_input().strip())
    w_counter = Counter(w)

    if len(w_counter.keys()) == 1:
        print "no answer"
        continue

    shift_found = False
    replace = {}
    set_replace_keys = set([])
    for i in xrange(len(w) - 1, 0, -1):
        for j in xrange(i - 1, -1, -1):
            if w[i] > w[j]:
                if j not in set_replace_keys:
                    replace[j] = w[i]
                    set_replace_keys.add(j)
                if i - j == 1:
                    shift_found = True
                    break
        if shift_found:
            break

    if shift_found:
        j = max(replace.keys())
        temp = replace[j]

        w.reverse()
        w.remove(temp)
        w.reverse()
        w.insert(j, temp)
        w = w[:(j + 1)] + sorted(w[(j + 1):])
        print ''.join(w)

    else:
        print "no answer"
        continue

print timeit.default_timer() - start
