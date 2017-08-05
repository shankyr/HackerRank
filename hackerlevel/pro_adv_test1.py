import heapq


def maxMin(operations, x):
    min_arr = []
    max_arr = []

    ans = []
    for ind in xrange(len(x)):
        if operations[ind] == "push":
            heapq.heappush(min_arr, x[ind])
            heapq.heappush(max_arr, x[ind] * -1)
        else:
            min_arr.remove(x[ind])
            max_arr.remove(x[ind] * -1)

        if len(min_arr) != 0:
            ans.append(long(min_arr[0] * max_arr[0] * -1))
        else:
            ans.append(long(0))

    return ans

print maxMin(['push', 'push', 'push', 'pop'], [1, 2, 3, 1])
print maxMin(['push', 'push'], [3, 2])




