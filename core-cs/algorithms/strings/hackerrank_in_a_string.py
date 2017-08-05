import timeit

start = timeit.default_timer()

queries = int(raw_input())

for q in xrange(queries):
    s = list(raw_input().strip())
    s_set = set(s)

    ref_str = list("hackerrank")

    ans = "YES"
    for letter in ref_str:
        if letter in s_set:
            ind = s.index(letter)
            s = s[ind + 1:]
            s_set = set(s)
        else:
            ans = "NO"

    print ans

print timeit.default_timer() - start
