# 30/41 tests passed

import sys
from operator import add
import timeit

sys.setrecursionlimit(100000)

start = timeit.default_timer()


def is_one_row_or_col_matrix_palindrome(arr, l, flag):
    area = 0
    num_of_odds = 0
    temp_c_arr = [0] * 10

    for val in arr:
        temp_c_arr[val] += 1

    for ind1 in xrange(10):
        area += temp_c_arr[ind1]

        if temp_c_arr[ind1] & 1:
            num_of_odds += 1

    if num_of_odds in (0, 1):
        if area > 1 and area - temp_c_arr[0] in (0, 1):
            print 1
            print 0, 0, 0, 0
            sys.exit(0)

        else:
            if flag == "row-m":
                print l
                print 0, 0, 0, l - 1
            else:
                print l
                print 0, 0, l - 1, 0
            sys.exit(0)


# function to get elements counter for every sub-matrix formulated
# it re-uses already computed elements array to generate for new sub-matrix
def get_counter_arr(arr, r_c_blk, s1, t1, s2, t2):
    if s1 == s2:
        try:
            c_arr_n = list(r_c_blk[(s1, t1, s2, t2)])
            return c_arr_n

        except KeyError:
            try:
                c_arr_n = list(r_c_blk[(s1, t1, s2, t2 - 1)])

            except KeyError:
                c_arr_n = get_counter_arr(arr, r_c_blk, s1, t1, s2, t2 - 1)

            c_arr_n[arr[s2][t2]] += 1

            r_c_blk[(s1, t1, s2, t2)] = c_arr_n
            return c_arr_n

    # adding last row
    if s1 == 0 and t1 == 0:
        try:
            c_arr1 = list(r_c_blk[(0, 0, s2 - 1, t2)])
        except KeyError:
            c_arr1 = get_counter_arr(arr, r_c_blk, 0, 0, s2 - 1, t2)
        try:
            c_arr2 = list(r_c_blk[(s2, 0, s2, t2)])
        except KeyError:
            c_arr2 = get_counter_arr(arr, r_c_blk, s2, 0, s2, t2)

        c_arr_n = [0] * 10
        for ind3 in xrange(10):
            c_arr_n[ind3] = c_arr1[ind3] + c_arr2[ind3]

        r_c_blk[(s1, t1, s2, t2)] = c_arr_n

        return c_arr_n

    # subtracting column
    elif s1 == 0 and t1 > 0:
        try:
            c_arr1 = list(r_c_blk[(0, 0, s2, t2)])
        except KeyError:
            c_arr1 = get_counter_arr(arr, r_c_blk, 0, 0, s2, t2)
        try:
            c_arr2 = list(r_c_blk[(0, 0, s2, t1 - 1)])
        except KeyError:
            c_arr2 = get_counter_arr(arr, r_c_blk, 0, 0, s2, t1 - 1)

        c_arr_n = [0] * 10
        for ind3 in xrange(10):
            c_arr_n[ind3] = c_arr1[ind3] - c_arr2[ind3]

        r_c_blk[(s1, t1, s2, t2)] = c_arr_n

        return c_arr_n

    # subtracting row
    elif s1 > 0 and t1 == 0:
        try:
            c_arr1 = list(r_c_blk[(0, 0, s2, t2)])
        except KeyError:
            c_arr1 = get_counter_arr(arr, r_c_blk, 0, 0, s2, t2)
        try:
            c_arr2 = list(r_c_blk[(0, 0, s1 - 1, t2)])
        except KeyError:
            c_arr2 = get_counter_arr(arr, r_c_blk, 0, 0, s1 - 1, t2)

        c_arr_n = [0] * 10
        for ind3 in xrange(10):
            c_arr_n[ind3] = c_arr1[ind3] - c_arr2[ind3]

        r_c_blk[(s1, t1, s2, t2)] = c_arr_n

        return c_arr_n

    # subtracting column
    else:
        try:
            c_arr1 = list(r_c_blk[(s1, 0, s2, t2)])
        except KeyError:
            c_arr1 = get_counter_arr(arr, r_c_blk, s1, 0, s2, t2)
        try:
            c_arr2 = list(r_c_blk[(s1, 0, s2, t1 - 1)])
        except KeyError:
            c_arr2 = get_counter_arr(arr, r_c_blk, s1, 0, s2, t1 - 1)

        c_arr_n = [0] * 10
        for ind3 in xrange(10):
            c_arr_n[ind3] = c_arr1[ind3] - c_arr2[ind3]

        r_c_blk[(s1, t1, s2, t2)] = c_arr_n

        return c_arr_n


def is_palindrome(c_arr, ans, i2, j2, k2, l2):
    num_of_odds = 0
    area = 0

    for ind2 in xrange(10):
        area += c_arr[ind2]

        if c_arr[ind2] & 1:
            num_of_odds += 1

    # check if its a palindrome
    if num_of_odds in (0, 1):

        # check number of non-zero elements to pick valid palindrome
        if area > 1 and area - c_arr[0] > 1:
            ans[area] = i2, j2, k2, l2


def generate_sub_matrices(arr, s, t, n2, m2, row_col_blocks, ans):

    row_grow = s
    while row_grow <= n2:

        # for every top-left row position, identify the best possible
        # right-bottom position that forms a sub-matrix of size bigger
        # than already identified size
        col_grow = t + (max(ans.keys()) / (row_grow - s + 1))
        while col_grow <= m2:
            try:
                c_arr = list(row_col_blocks[(s, t, row_grow, col_grow)])
            except KeyError:
                c_arr = get_counter_arr(arr, row_col_blocks, s, t, row_grow, col_grow)

            is_palindrome(c_arr, ans, s, t, row_grow, col_grow)

            col_grow += 1

        row_grow += 1


def initialize_matrix_dict(arr, n1, m1, blk):
    for i1 in xrange(n1):
        for j1 in xrange(m1):
            c_arr = [0] * 10
            c_arr[arr[i1][j1]] = 1

            blk[(i1, j1, i1, j1)] = c_arr


n, m = map(int, raw_input().strip().split(' '))

inp = []
for rd in xrange(n):
    inp.append(map(int, raw_input().strip().split(' ')))

answer = {1: (0, 0, 0, 0)}

# if its a row matrix
if n == 1:
    is_one_row_or_col_matrix_palindrome(inp[0], m, "row-m")

# if its a column matrix
if m == 1:
    temp_col = reduce(add, inp)
    is_one_row_or_col_matrix_palindrome(temp_col, n, "col-m")

# elements (0 to 9) counter array for all possible sub-matrices
# are stored in a dictionary with top-left and right-bottom positions
# as key and their elements counter as value
sub_matrices = {}
initialize_matrix_dict(inp, n, m, sub_matrices)

# calling the logic for every position in matrix
# with checks to skip positions that can only
# generate a matrix of size lesser than already observer size
for p1 in xrange(n):
    if max(answer.keys()) < (n - p1) * m:
        for q1 in xrange(m):
            if max(answer.keys()) < (n - p1) * (m - q1):
                generate_sub_matrices(inp, p1, q1, n - 1, m - 1, sub_matrices, answer)
            else:
                break
    else:
        break

# print answer
max_area = max(answer.keys())
print max_area
print answer[max_area][0], answer[max_area][1], answer[max_area][2], answer[max_area][3]

# print timeit.default_timer() - start
