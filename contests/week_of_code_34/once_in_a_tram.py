# 7/7 tests passed


def onceInATram(x):
    # Complete this function
    # print x

    first_3 = x / 1000
    last_3 = x % 1000

    # print first_3, last_3

    sum_first_3 = sum(map(int, list(str(first_3))))
    last_3 += 1
    sum_last_3 = sum(map(int, list(str(last_3))))

    while sum_last_3 != sum_first_3:
        last_3 += 1

        if last_3 < 1000:
            sum_last_3 = sum(map(int, list(str(last_3))))
        else:
            last_3 = 0
            sum_last_3 = sum(map(int, list(str(last_3))))
            first_3 += 1
            sum_first_3 += 1

    return first_3 * 1000 + last_3


if __name__ == "__main__":
    x = int(raw_input().strip())
    result = onceInATram(x)
    print result
