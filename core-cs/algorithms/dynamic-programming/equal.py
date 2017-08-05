import sys
import timeit

start = timeit.default_timer()

sys.setrecursionlimit(100000)


def calc_operations(int_arr):
    print int_arr
    if len(int_arr) == 1:
        return 0
    else:
        lower_val = int_arr[0]
        higher_val = lower_val
        higher_index = 0
        for ind in xrange(len(int_arr)):
            if higher_val < int_arr[ind]:
                higher_val = int_arr[ind]
                higher_index = ind
                break

        if higher_index == 0:
            return 0

        ops_selection = {abs(higher_val - lower_val - 1): 1, \
                         abs(higher_val - lower_val - 2): 2, \
                         abs(higher_val - lower_val - 5): 5}

        best_selection = ops_selection[min(ops_selection.keys())]
        # print best_selection

        ans = (higher_val - lower_val) / best_selection
        rem = (higher_val - lower_val) % best_selection

        increment = ans * best_selection
        if increment == 0:
            increment = best_selection
        # print ans, rem

        for ind in xrange(len(int_arr)):
            if ind == higher_index:
                continue
            int_arr[ind] += increment

        int_arr.sort()

        return ans + calc_operations(int_arr)


tests = int(raw_input().strip())

for test in xrange(tests):
    n = int(raw_input().strip())
    intern_arr = map(int, raw_input().strip().split(' '))
    intern_arr_sorted = sorted(intern_arr)
    # print intern_arr_sorted
    print calc_operations(intern_arr_sorted)

    print timeit.default_timer() - start
