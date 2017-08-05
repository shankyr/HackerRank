#!/bin/python


tests = int(raw_input().strip())

for test in xrange(tests):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]

    ans_found = False
    rep = {}

    if k == 0:
        for num in xrange(1, n + 1):
            print num,
        print
        continue

    for num in xrange(1, n + 1):
        num_added = False

        if num - k <= 0 and num + k > n:
            print "-1"
            ans_found = True
            break
        else:

            if num - k > 0:
                try:
                    rep[num - k]
                except:
                    rep[num - k] = num
                    num_added = True

            if not num_added:
                if num + k <= n:
                    try:
                        rep[num + k]
                        print "-1"
                        ans_found = True
                        break
                    except:
                        rep[num + k] = num
                else:
                    print "-1"
                    ans_found = True
                    break

    if not ans_found:
        for pos in sorted(rep.keys()):
            print rep[pos],
        print
