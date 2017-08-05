import timeit
import heapq

start = timeit.default_timer()

N, K = map(int, raw_input().strip().split(' '))
luck_bal = 0
imp_loses = []
imp_wins = []

for i in xrange(N):
    luck, comp_type = map(int, raw_input().strip().split(' '))

    if comp_type == 0:
        luck_bal += luck
    else:
        heapq.heappush(imp_loses, luck)

        if len(imp_loses) > K:
            imp_wins.append(heapq.heappop(imp_loses))

for j in xrange(len(imp_loses)):
    luck_bal += imp_loses[j]

for k in xrange(len(imp_wins)):
    luck_bal -= imp_wins[k]

print luck_bal

print timeit.default_timer() - start
