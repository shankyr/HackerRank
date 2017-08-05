
n = int(raw_input().strip())
int_to_str = {}
str_to_pos = {}
for i in xrange(n):
    x, st = raw_input().strip().split()

    try:
        int_to_str[int(x)].append(st)
    except KeyError:
        int_to_str[int(x)] = [st]

    try:
        str_to_pos[(int(x), st)].append(i)
    except KeyError:
        str_to_pos[(int(x), st)] = [i]

# print int_to_str
# print str_to_pos

half = n / 2
for ind in xrange(100):
    try:
        words = int_to_str[ind]
        for word in words:
            positions = str_to_pos[(ind, word)]
            if positions[0] > half - 1:
                print word,
            else:
                print "-",

            del positions[0]
            str_to_pos[(ind, word)] = positions

    except KeyError:
        pass
