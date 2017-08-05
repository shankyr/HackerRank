#!/bin/python

from collections import Counter


tests = int(raw_input().strip())

for test in xrange(tests):
    n = int(raw_input().strip())
    b = raw_input().strip()

    b_list = list(b)
    b_char_count = Counter([ch for ch in b_list if ch != '_'])

    if len(b_char_count.keys()) == 0:
        print "YES"

    else:
        if len([val for val in b_char_count.values() if val == 1]) > 0:
            print "NO"
        else:
            if sum(val for val in b_char_count.values()) == n:
                mismatch = 0
                for ind in xrange(1, len(b_list) - 1):
                    if b_list[ind] != b_list[ind - 1] and b_list[ind] != b_list[ind + 1]:
                        print "NO"
                        mismatch += 1
                        break
                if not mismatch:
                    print "YES"
            else:
                print "YES"
