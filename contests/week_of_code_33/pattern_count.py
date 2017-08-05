# all tests passed

import re


def pattern_count(s):
    # Complete this function
    return len(re.findall("1(?=(0+)1)", s))

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = pattern_count(s)
    print(result)
