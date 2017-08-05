# 3/30 tests passed


def calc_sub(temp_arr):
    # print temp_arr
    target_sum = 0
    sub_arr_count = 0

    temp_arr_len = len(temp_arr)
    temp_sum = 0

    for i in xrange(temp_arr_len):
        if temp_arr[i] == 0:
            continue

        temp_sum += temp_arr[i]

        if temp_sum == target_sum:
            sub_arr_count += 1

    # print sub_arr_count
    return sub_arr_count


def calc_answer(arr, x, y, n):
    temp_arr = [0] * n
    zero_positions = []

    total_sum = 0

    for i in xrange(n):
        if arr[i] == x:
            temp_arr[i] = 1
        elif arr[i] == y:
            temp_arr[i] = -1
        else:
            temp_arr[i] = 0

    for i in xrange(n):
        total_sum += calc_sub(temp_arr[i:])
        if temp_arr[i] == 0:
            zero_positions.append(i)

    # print "from subs", total_sum

    # print "zero_positions", zero_positions

    zeros_len = len(zero_positions)
    count = 1
    for i in xrange(zeros_len):
        j = i + 1
        if j < zeros_len:
            if zero_positions[i] + 1 == zero_positions[j]:
                count += 1
                continue

        # print "count", count
        total_sum += count * (count + 1) / 2
        count = 1

    return total_sum


if __name__ == "__main__":
    n, q = raw_input().strip().split(' ')
    n, q = [int(n), int(q)]
    arr = map(int, raw_input().strip().split(' '))

    arr_set = set(arr)

    answers = {}

    for a0 in xrange(q):
        x, y = raw_input().strip().split(' ')
        x, y = [int(x), int(y)]
        # Write Your Code Here

        try:
            print answers[(x, y)]
            continue
        except KeyError:
            if x not in arr_set and y not in arr_set:
                ans = n * (n + 1) / 2
                answers[(x, y)] = ans
                answers[(y, x)] = ans
            else:
                ans = calc_answer(arr, x, y, n)
                answers[(x, y)] = ans
                answers[(y, x)] = ans

            print ans
