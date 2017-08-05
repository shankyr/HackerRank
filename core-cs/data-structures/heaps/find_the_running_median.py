import heapq
import timeit

start = timeit.default_timer()


def add_number(num, lowers, highers):
    if not lowers or num < lowers[0] * -1:
        heapq.heappush(lowers, num * -1)
    else:
        heapq.heappush(highers, num)

    return lowers, highers


def balance_heaps(lowers, highers):
    smaller_heap = lowers if len(lowers) < len(highers) else highers
    bigger_heap = highers if len(highers) > len(lowers) else lowers

    if len(bigger_heap) - len(smaller_heap) > 1:
        # print "BEFORE: smaller, bigger", smaller_heap, bigger_heap
        heapq.heappush(smaller_heap, heapq.heappop(bigger_heap) * -1)

    # print "AFTER: smaller, bigger", smaller_heap, bigger_heap
    return lowers, highers


def get_median(lowers, highers):
    # print lowers, highers
    if len(lowers) == len(highers):
        return float(lowers[0] * -1 + highers[0]) / 2
    else:
        bigger_heap = highers if len(highers) > len(lowers) else lowers
        return abs(bigger_heap[0])


n = int(raw_input().strip())
lowers = []
highers = []

for i in xrange(n):
    number = int(raw_input().strip())
    lowers, highers = add_number(number, lowers, highers)
    lowers, highers = balance_heaps(lowers, highers)
    print "%.1f" % get_median(lowers, highers)

print timeit.default_timer() - start
