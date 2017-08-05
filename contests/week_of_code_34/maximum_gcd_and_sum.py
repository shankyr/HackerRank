# 28/28 tests passed

from collections import Counter


def maximum_gcd_pair(big_arr, A_set, B_set):

    big_arr_counter = Counter(big_arr)

    s = set(big_arr)
    m = max(big_arr)

    i = m

    while i > 0:
        a = i
        count = 0
        temp_arr = set([])
        while a <= m:
            if a in s:
                count += big_arr_counter[a]
                temp_arr.add(a)
            a += i

        if count >= 2:
            A_elems = A_set & temp_arr
            B_elems = B_set & temp_arr

            if len(A_elems) != 0 and len(B_elems) != 0:
                return max(A_elems) + max(B_elems)

        i -= 1


def maximumGcdAndSum(A, B):
    # Complete this function

    A_set, B_set = set(A), set(B)
    big_arr = A + B
    return maximum_gcd_pair(big_arr, A_set, B_set)

if __name__ == "__main__":
    n = int(raw_input().strip())
    A = map(int, raw_input().strip().split(' '))
    B = map(int, raw_input().strip().split(' '))
    res = maximumGcdAndSum(A, B)
    print res
