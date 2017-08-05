import timeit

start = timeit.default_timer()


def number_needed(a, b):
    l1, l2 = len(a), len(b)
    total = l1 + l2

    if l1 < l2:
        s1 = list(a)
        s1.sort()
        s2 = list(b)
        s2.sort()
    else:
        s1 = list(b)
        s1.sort()
        s2 = list(a)
        s2.sort()

    for i in xrange(len(s1)):
        for j in xrange(len(s2)):
            if s1[i] == s2[j]:
                total -= 2
                s2.remove(s2[j])
                break
            elif s1[i] < s2[j]:
                break

    return total


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

print timeit.default_timer() - start
