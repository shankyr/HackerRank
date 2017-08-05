import timeit

start = timeit.default_timer()


def is_prime(n):

    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    else:
        i = 5
        k = 2
        while i <= n ** 0.5:
            if n % i == 0:
                return False
            i += k
            k = 6 - k

        return True


tests = int(raw_input().strip())

for test in xrange(tests):
    num = int(raw_input().strip())

    if is_prime(num):
        print "Prime"
    else:
        print "Not prime"

print timeit.default_timer() - start
