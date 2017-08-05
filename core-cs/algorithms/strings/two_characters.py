import timeit
from collections import Counter
from itertools import combinations


start = timeit.default_timer()

n = int(raw_input().strip())
s = list(raw_input().strip())

# corner cases where answer is 0
if n == 1 or len(set(s)) == 1:
    print "0"
    exit()


# deleting all adjacent repeats
while True:
    adj_repetition = 0
    for ind in xrange(len(s) - 1):
        if s[ind] == s[ind + 1]:
            elem = s[ind]
            s = [alpha for alpha in s if alpha != elem]
            adj_repetition += 1
            break

    if adj_repetition == 0:
        break


s_counter = Counter(s)
distinct_alpha = len(s_counter.keys())

# picking all the possible 2 alphabet from remaining alphabet
alpha_comb = list(combinations(s_counter.keys(), 2))

ans = []
for comb in alpha_comb:
    valid_s = True
    possible_s = [alpha for alpha in s if alpha in comb]

    # checking if the string formed with 2 alphabet is valid
    for ind in xrange(len(possible_s) - 1):
        if possible_s[ind] == possible_s[ind + 1]:
            valid_s = False
            break

    # if valid, write its length to answer list
    if valid_s:
        ans.append(len(possible_s))


try:
    # output the maximum length of all valid strings that can be formed
    print max(ans)
except ValueError:
    # if no valid string can be formed; then output 0
    print "0"

print timeit.default_timer() - start
