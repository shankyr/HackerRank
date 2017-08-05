
def calc_result(s1):
    converter = ['1'] * len(s1)
    converter = ''.join(converter)

    return s1 + bin(int(s1, 2) ^ int(converter, 2))[2:]


q = int(raw_input().strip())

for test in xrange(q):
    s = '0'
    ind = int(raw_input().strip())

    while len(s) < ind + 1:
        print "len(s) < ind + 1:", len(s), ind + 1
        print "s", s
        s = calc_result(s)

    print "s", s
    print s[ind]


