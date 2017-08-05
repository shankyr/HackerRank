import timeit

start = timeit.default_timer()


def add_num(num, new):
    low, high = 0, len(num) - 1
    # print num, low, high

    if not num:
        num.append(new)
        return num
    if new < num[low]:
        num.insert(0, new)
        return num
    if new > num[high]:
        num.append(new)
        return num

    while low <= high:
        mid = (low + high) / 2
        if new < num[mid]:
            high = mid - 1
        else:
            low = mid + 1

    num.insert(low, new)
    return num


def print_median(num):
    length = len(num)
    if length % 2 == 0:
        answer = float(num[length / 2] + num[(length / 2) - 1]) / 2
        print "%.1f" % answer
    else:
        answer = num[(length - 1) / 2]
        print "%.1f" % answer


n = int(raw_input().strip())
num = []

for i in xrange(n):
    new = int(raw_input().strip())
    num = add_num(num, new)
    print_median(num)

print timeit.default_timer() - start
