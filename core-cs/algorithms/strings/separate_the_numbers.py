
tests = int(raw_input().strip())

for test in xrange(tests):
    string = list(raw_input().strip())

    # print string

    first_int, second_int = 0, 0

    ans = "YES"
    if len(string) == 1 or int(string[0]) == 0:
        ans = "NO"

    else:
        l = len(string)
        if l % 2 == 0:
            digits_checker = (l / 2) - 1
        else:
            digits_checker = (l / 2)

        for digits in xrange(digits_checker + 1):

            first = string[:digits + 1]
            len_of_first = len(first)

            first_num = int(''.join(first))

            if first_num == (10 ** (digits + 1)) - 1:
                len_of_first += 1

            second = string[digits + 1: digits + 1 + len_of_first]

            second_num = int(''.join(second))

            # print "first_num", first_num
            # print "second_num", second_num

            if second_num - first_num == 1:
                first_int, second_int = first_num, second_num

    if (first_int, second_int) == (0, 0):
        ans = "NO"
    else:
        prev_int = second_int
        prev_len = len(str(second_int))

        start = len(str(first_int)) + len(str(second_int))
        curr_int = 0

        while start < l:

            if prev_int == (10 ** prev_len) - 1:
                prev_len += 1

            curr = string[start:start + prev_len]
            curr_int = int(''.join(curr))

            if curr_int - prev_int != 1:
                ans = "NO"
                break

            prev_int = curr_int
            prev_len = len(str(curr_int))
            start += prev_len

    # print "first_int, second_int", first_int, second_int
    # print "ans", ans

    if ans == "YES":
        print ans, first_int
    else:
        print ans
