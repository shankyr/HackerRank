n = int(raw_input().strip())

cakes = map(int, raw_input().strip().split(' '))
cakes_eating_order = sorted(cakes, reverse=True)

ans = 0
for ind in xrange(n):
    ans += (2 ** ind) * cakes_eating_order[ind]

print ans
