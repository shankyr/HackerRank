import heapq

n = int(raw_input())

orders = []
for i in xrange(n):
    t, d = map(int, raw_input().strip().split(' '))
    heapq.heappush(orders, (t + d, i))

for i in xrange(n):
    print heapq.heappop(orders)[1] + 1,
