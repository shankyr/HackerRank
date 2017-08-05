# Enter your code here. Read input from STDIN. Print output to STDOUT

X = int(raw_input().strip())
N = int(raw_input().strip())


def find_max_num(X, N, i):
    if i ** N == X:
        return i
    elif i ** N > X:
        return i - 1
    else:
        return find_max_num(X, N, i + 1)


def num_of_ways(X, N, maxNum):
    if X == 0:
        return 1
    elif X < 0 or maxNum == 0:
        return 0
    else:
        return num_of_ways(X - maxNum ** N, N, maxNum - 1) + num_of_ways(X, N, maxNum - 1)


mNum = find_max_num(X, N, 1)
# print mNum
print num_of_ways(X, N, mNum)
