import timeit

start = timeit.default_timer()


def is_matched(expression):
    left = {'{': 0, '[': 0, '(': 0}
    right = {'}': 0, ']': 0, ')': 0}

    s = list(expression)
    l = len(s)

    if l % 2 != 0:
        return False
    else:
        for i in xrange(l):
            try:
                left[s[i]] += 1
            except:
                right[s[i]] += 1

        if right['}'] == left['{'] and right[']'] == left['['] and right[')'] == left['(']:
            return True
        else:
            return False


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression):
        print "YES"
    else:
        print "NO"

print timeit.default_timer() - start
