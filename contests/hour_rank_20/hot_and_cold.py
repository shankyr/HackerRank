

c1, c2, h1, h2 = map(int, raw_input().strip().split(' '))

lower_bound = max(c1, c2)
higher_bound = min(h1, h2)

if lower_bound <= higher_bound:
    print "YES"
else:
    print "NO"

