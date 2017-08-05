import timeit

start = timeit.default_timer()


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        k = n / 2
        if n % 2 == 0:
            return fibonacci(k) * (2 * fibonacci(k + 1) - fibonacci(k))
        else:
            return fibonacci(k + 1) ** 2 + fibonacci(k) ** 2

n = int(raw_input())
print(fibonacci(n))

print timeit.default_timer() - start
