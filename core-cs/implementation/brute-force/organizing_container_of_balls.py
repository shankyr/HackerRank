import timeit

start = timeit.default_timer()

query = int(raw_input().strip())

for q in xrange(query):
    n = int(raw_input().strip())
    c = []
    b = []
    for i in xrange(n):
        c.append(list(map(int, raw_input().strip().split(' '))))

    for i in xrange(n):
        total_balls_for_given_type = 0
        for j in xrange(n):
            total_balls_for_given_type += c[j][i]

        b.append(total_balls_for_given_type)

    ans_found = False
    for i in xrange(n):
        total_balls_for_given_container = sum(c[i])
        if total_balls_for_given_container not in b:
            print "Impossible"
            ans_found = True
            break
        else:
            b.remove(total_balls_for_given_container)

    if not ans_found:
        print "Possible"

print timeit.default_timer() - start
