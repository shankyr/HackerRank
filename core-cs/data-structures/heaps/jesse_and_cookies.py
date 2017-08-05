import heapq
import timeit

start = timeit.default_timer()
print start

n, k = map(int, raw_input().strip().split(' '))
cookies = map(int, raw_input().strip().split(' '))
temp = [-1]

heapq.heapify(cookies)

ops = 0
while True:
    sweet1 = heapq.heappop(cookies)

    if sweet1 >= k:
        print ops
        break

    if cookies:
        sweet2 = heapq.heappop(cookies)
        new_sweet = sweet1 + 2 * sweet2
        heapq.heappush(cookies, new_sweet)
        ops += 1
    else:
        print -1
        break

print timeit.default_timer() - start

