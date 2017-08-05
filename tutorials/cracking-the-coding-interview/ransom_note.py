import timeit

start = timeit.default_timer()


def ransom_note(magazine, ransom):
    magzD = {}
    ransD = {}

    for i in xrange(m):
        if magazine[i] in magzD:
            magzD[magazine[i]] += 1
        else:
            magzD[magazine[i]] = 1

    for key in ransom:
        if key in magzD:
            if magzD[key] == 0:
                return False
            else:
                magzD[key] -= 1
        else:
            return False

    return True


m, n = map(int, raw_input().strip().split(' '))

magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')

answer = ransom_note(magazine, ransom)

if answer:
    print "Yes"
else:
    print "No"

print timeit.default_timer() - start
