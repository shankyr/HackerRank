from collections import Counter
import sys
import timeit

sys.setrecursionlimit(10000)
start = timeit.default_timer()


def calc_func_value(s_arr, sub_s_hash):

    if len(s_arr) == 0:
        return 0

    s_str = ''.join(s_arr)
    if s_str not in sub_s_hash:
        sub_s_hash.add(s_str)
        return len(s_arr) ** len(Counter(s_arr).keys()) + \
                calc_func_value(s_arr[:-1], sub_s_hash) + \
                calc_func_value(s_arr[1:], sub_s_hash)
    else:
        return 0

T = int(raw_input().strip())

for t in xrange(T):
    s = raw_input().strip()
    s_list = list(s)

    sub_string_hash = set([])
    print calc_func_value(s_list, sub_string_hash)


print timeit.default_timer() - start
