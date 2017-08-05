
n, k = map(int, raw_input().strip().split(' '))

costs = map(int, raw_input().strip().split(' '))
costs.sort()

spoiler = 0
friends = 1
total_cost = 0
for i in xrange(n - 1, -1, -1):

    if friends <= k:
        total_cost += (spoiler + 1) * costs[i]
        friends += 1
    else:
        friends = 2
        spoiler += 1
        total_cost += (spoiler + 1) * costs[i]

print total_cost
